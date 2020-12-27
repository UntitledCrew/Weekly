import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static class Node {
		int r;
		int c;

		public Node(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}
	
	private static Node[] queue;
	private static int front;
	private static int rear;
	private static int qSize;
	
	private static int N;
	private static int M;
	private static int[][] miro;
	private static int[][] visited;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		miro = new int[N][M];
		visited = new int[N][M];

		for (int i = 0; i < miro.length; i++) {
			String line = br.readLine();
			for (int j = 0; j < miro[i].length; j++) {
				miro[i][j] = line.charAt(j) - '0';
			}
		}

		/* *** 구현 부분 *** */
		queue = new Node[200];
		qSize = queue.length;
		front = 0;
		rear = 0;
		
		// 첫 번째 데이터를 큐에 넣자
		Node node = new Node(0, 0);
		enQueue(node);
		visited[0][0] = 1;
		
		// 큐가 빌 때까지
		while(!isEmpty()) {
			// 큐에서 하나의 노드를 꺼내어 방문한다.
			Node vnode = deQueue();
			int vr = vnode.r;
			int vc = vnode.c;
			
			// 방문한 노드의 주변 노드들 중 조건에 만족하는 노드를 큐에 넣는다
			if(vc+1 < M && miro[vr][vc+1] == 1 && visited[vr][vc+1] == 0) {	// 우
				if(visited[vr][vc+1] != 0 && visited[vr][vc+1] > visited[vr][vc]) {
					visited[vr][vc+1] = visited[vr][vc] + 1;
					enQueue(new Node(vr, vc+1));
				}
				else {
					visited[vr][vc+1] = visited[vr][vc] + 1;
					enQueue(new Node(vr, vc+1));
				}
			}
			if(vr+1 < N && miro[vr+1][vc] == 1 && visited[vr+1][vc] == 0) {	// 하
				if(visited[vr+1][vc] != 0 && visited[vr+1][vc] > visited[vr][vc]) {
					visited[vr+1][vc] = visited[vr][vc] + 1;
					enQueue(new Node(vr+1, vc));
				}
				else {
					visited[vr+1][vc] = visited[vr][vc] + 1;
					enQueue(new Node(vr+1, vc));
				}
					
			}
			if(0 <= vr-1 && miro[vr-1][vc] == 1 && visited[vr-1][vc] == 0) {	// 상
				if(visited[vr-1][vc] != 0 && visited[vr-1][vc] > visited[vr][vc]) {
					visited[vr-1][vc] = visited[vr][vc] + 1;
					enQueue(new Node(vr-1, vc));
				}
				else {
					visited[vr-1][vc] = visited[vr][vc] + 1;
					enQueue(new Node(vr-1, vc));
				}
			}
			if(0 <= vc-1 && miro[vr][vc-1] == 1 && visited[vr][vc-1] == 0) {	// 좌
				if(visited[vr][vc-1] != 0 && visited[vr][vc-1] > visited[vr][vc]) {
					visited[vr][vc-1] = visited[vr][vc] + 1;
					enQueue(new Node(vr, vc-1));
				}
				else {
					visited[vr][vc-1] = visited[vr][vc] + 1;
					enQueue(new Node(vr, vc-1));
				}
			}
		}
		System.out.println(visited[N-1][M-1]);
	} // end of main
	
	public static boolean isFull() {
		if( (rear+1)%qSize == front )
			return true;
		else 
			return false;
	}
	
	public static boolean isEmpty() {
		if( rear == front )
			return true;
		else 
			return false;
	}
	
	public static boolean enQueue(Node node) {
		if(isFull()) {
			System.out.println("큐가 가득 찼습니다 !");
			return false;
		} else {
			rear = ++rear % qSize;
			queue[rear] = node;
			return true;
		}
	}
	
	public static Node deQueue() {
		if(isEmpty()) {
			System.out.println("큐가 비어서 꺼낼 노드가 없습니다 !");
			return null;
		} else {
			front = ++front % qSize;
			return queue[front];
		}
	}
	
	public static Node peek() {
		if(isEmpty()) {
			System.out.println("큐가 비어 노드 데이터를 읽을 수 없습니다.");
			return null;
		} else {
			return queue[(front+1)%qSize];
		}
	}
	
} // end of class