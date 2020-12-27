import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.StringTokenizer;


public class Main {
	private static int M;
	private static int N;
	private static int V;
	private static ArrayList<ArrayList<Integer>> adjList;
	private static boolean[] visited;
	private static StringBuilder sb;
	private static LinkedList<Integer> q;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		sb = new StringBuilder();
		
		N = Integer.parseInt(st.nextToken());	// 정점의 개수
		M = Integer.parseInt(st.nextToken());	// 간선의 개수
		V = Integer.parseInt(st.nextToken());	// 시작 정점 번호
		
		adjList = new ArrayList<ArrayList<Integer>>();
		
		for (int i = 0; i <= N; i++) {
			adjList.add(new ArrayList<Integer>());
		}
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			
			adjList.get(start).add(end);
			adjList.get(end).add(start);
		}
		
		for (int i=0; i < adjList.size(); i++) {
			Collections.sort(adjList.get(i));
		}
		
		visited = new boolean[N+1];
		visited[V] = true;
		sb.append(V).append(' ');
		dfs(V);
		sb.append('\n');
		
		q = new LinkedList<Integer>();
		visited = new boolean[N+1];
		visited[V] = true;
		sb.append(V).append(' ');
		q.add(V);
		bfs();
		
		System.out.println(sb);
	}
	
	public static void dfs(int x) {
		for (int i = 0; i < adjList.get(x).size(); i++ ) {
			if (!visited[adjList.get(x).get(i)]) {
				visited[adjList.get(x).get(i)] = true;
				sb.append(adjList.get(x).get(i)).append(' ');
				dfs(adjList.get(x).get(i));
			}
		}
	}
	
	public static void bfs() {
		while(!q.isEmpty()) {
			int data = q.poll();
			
			for (int i = 0; i < adjList.get(data).size(); i++) {
				if (!visited[adjList.get(data).get(i)]) {
					visited[adjList.get(data).get(i)] = true;
					sb.append(adjList.get(data).get(i)).append(' ');
					q.add(adjList.get(data).get(i));
				}
			}
		}
	}
}



