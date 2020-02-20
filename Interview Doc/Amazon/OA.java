import java.util.*;
import java.io.*; 
// import java.lang.*;

public class OA {
	public int[] MoviesOnFlight(int[] movies, int d) {
		Map<Integer, List<Integer>> index = new HashMap<>();
		int length = movies.length;
		if (length == 0) {
			return new int[] {-1, -1};
		}
		for(int i = 0; i < length; i++) {
			index.putIfAbsent(movies[i], new ArrayList<Integer>());
			index.get(movies[i]).add(i);
		}

		Arrays.sort(movies);
		int l = 0;
		int r = length - 1;
		int max = 0;
		int target = d - 30;
		int[] res = new int[] {-1, -1};
		while(l < r) {
			int sum = movies[l] + movies[r];
			if(sum == target) {
				res[0] = movies[l];
				res[1] = movies[r];
				break;
			} else if (sum < target) {
				if(max < sum) {
					res[0] = movies[l];
					res[1] = movies[r];
					max = sum;
				}
				l++;
			} else {
				r--;
			}
		}
		if (res[0] == -1 && res[1] == -1) {
			return res;
		}  
		if (res[0] == res[1]) {
	        return new int[]{map.get(res[0]).get(0), map.get(res[1]).get(1)};
	    } else {
	        int li = map.get(res[0]).get(0);
	        int ri = map.get(res[1]).get(0);
	        if(li<ri){
	            return new int[]{li,ri};
	        }else{
	            return new int[]{ri,li};
	        }
	    }	
	}

	private static int[] Find2Sum(int[] nums, int target) {
		Map<Integer, Integer> map = new HashMap<>();
		int max = Integer.MIN_VALUE;
		int[] res = new int[] {-1, -1};
		for(int i=0;i<nums.length;i++) {
			if(map.containsKey(nums[i])) {
				if(nums[i] > max || nums[map.get(nums[i])] > max) {
					res[0] = map.get(nums[i]);
					res[1] = i;
					max = Math.max(nums[i], nums[map.get(nums[i])]);
				}
			}
			map.put(target - nums[i], i);
		}
		return res;
	}

	public Node copyRandomList(Node head) {
        if(head == null) return null;
        Node copyhead = head;
        while(copyhead != null) {
            Node next = copyhead.next;
            copyhead.next = new Node(copyhead.val);
            copyhead.next.next = next;
            copyhead = next;
        }
        
        copyhead = head;
        while(copyhead != null) {
            if(copyhead.random != null) {
                copyhead.next.random = copyhead.random.next;
            }
            copyhead = copyhead.next.next;
        }
        
        Node newhead = head.next;
        Node tmp = newhead;
        while(tmp.next != null) {
            head.next = head.next.next;
            head = head.next;
            tmp.next = tmp.next.next;
            tmp = tmp.next;
        }
        head.next = head.next.next;
        return newhead;
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null) return l2;
		if(l2 == null) return l1;
		if(l1.val < l2.val){
			l1.next = mergeTwoLists(l1.next, l2);
			return l1;
		} else{
			l2.next = mergeTwoLists(l1, l2.next);
			return l2;
		}
    }

    public boolean isSubtree(TreeNode s, TreeNode t) {
        if (s == null) return false;
        if (isSame(s, t)) return true;
        return isSubtree(s.left, t) || isSubtree(s.right, t);
    }
    
    private boolean isSame(TreeNode s, TreeNode t) {
        if (s == null && t == null) return true;
        if (s == null || t == null) return false;
        
        if (s.val != t.val) return false;
        
        return isSame(s.left, t.left) && isSame(s.right, t.right);
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix == null || matrix.length < 1 || matrix[0].length <1) {	
            return false;
        }
        int col = matrix[0].length-1;
        int row = 0;
        while(col >= 0 && row <= matrix.length-1) {
            if(target == matrix[row][col]) {
                return true;
            } else if(target < matrix[row][col]) {
                col--;
            } else if(target > matrix[row][col]) {
                row++;
            }
        }
        return false;
    }

    public int uniquePairs(int[] nums, int target) {
    	Set<Integer> set = new HashSet<Integer>();
        Set<Integer> seen = new HashSet<Integer>();
        int count = 0;
        for(int num : nums){
            if(set.contains(target-num) && !seen.contains(num)){
                count++;
                seen.add(target-num);
                seen.add(num);
            }
            else if(!set.contains(num)){
                set.add(num);
            }
        }
        return count;
    }

    public static int[][] generateMatrix(int n) {
		int[][] ret = new int[n][n];
		int left = 0,top = 0;
		int right = n -1,down = n - 1;
		int count = 1;
		while (left <= right) {
			for (int j = left; j <= right; j ++) {
				ret[top][j] = count++;
			}
			top ++;
			for (int i = top; i <= down; i ++) {
				ret[i][right] = count ++;
			}
			right --;
			for (int j = right; j >= left; j --) {
				ret[down][j] = count ++;
			}
			down --;
			for (int i = down; i >= top; i --) {
				ret[i][left] = count ++;
			}
			left ++;
		}
		return ret;
	}

	public String mostCommonWord(String paragraph, String[] banned) {
        String[] words = paragraph.toLowerCase().split("\\W+");
        HashSet<String> set = new HashSet<>();
        Map<String, Integer> map = new HashMap<>();
        for(String word : banned) {
            set.add(word);
        }
        for(String word : words) {
            if(!set.contains(word)) {
                map.put(word, map.getOrDefault(word, 0) + 1);
            }
        }
        int max = 0;
        String res = "";
        for(String str : map.keySet()) {
            if(map.get(str) > max) {
                max = map.get(str);
                res = str;
            }
        }
        return res;
    }

    public Map<String, List<String>> favoritegenre(Map<String, List<String>> userMap, Map<String, List<String>> genreMap) {
	   	Map<String, List<String>> res = new HashMap<>();
	   	Map<String, String> songstogenre = new HashMap<>();
	   	
	   	for(String genre : genreMap.keySet()) {
	   		List<String> songs = genreMap.get(genre);
	   		if (songs.size() > 0) {
	   			for(String song : songs) {
		   			songstogenre.put(song, genre);
		   		}
	   		}
	   	}
	    Map<String, Integer> count = new HashMap();
	   	int max = 0;
	   	for(String user : userMap.keySet()) {
            count = new HashMap();
            max = 0;
            res.put(user, new ArrayList());
	   		List<String> songs = userMap.get(user);
	   		for(String song : songs) {
	   			if(songstogenre.containsKey(song)) {
	   				String genre = songstogenre.get(song);
		   			int c = count.getOrDefault(genre, 0) + 1;
		   			count.put(genre, c);
		            max = Math.max(c, max);
	   			}
	   		}
            for (String key : count.keySet()) {
                if (count.get(key) == max) {
                    res.get(user).add(key);
                }
            }
	   	}
	   	return res;
   }

    private TrieNode root;
    
    public List<String> productSuggestions(String[] repo, String query) {
        root = new TrieNode();
        
        for (String str : repo) {
            add(str);
        }
        int len = query.length();
        // mouse
        for (int i = len - 3; i <= len; i++) {
            search(query.substring(0, i));
        }
        
        return null;
    }
    
    private void add(String s) {
        TrieNode cur = root;
        for (char c : s.toCharArray()) {
            TrieNode next = cur.children.get(c);
            if (next == null) {
                next = new TrieNode();
                cur.children.put(c, next);
            }
            next.queue.offer(s);
            if (next.queue.size() > 3) {
                next.queue.poll();
            }
            cur = next;
            
        }
    }
    
    private List<String> search(String input) {
        List<String> res = new ArrayList<>();
        TrieNode p = root;
        for (char c : input.toCharArray()) {
            TrieNode child = p.children.get(c);
            if (child == null) { // if not found, return an empty 
                return new ArrayList<>();
            }
            p = child;
        }
        PriorityQueue<String> pq = new PriorityQueue<>(p.queue);
        int cnt = 0;
        while (!pq.isEmpty() && cnt < 3) {
            res.add(0, pq.poll());
        }
        System.out.println(res.toString());
        return res;
        
    }
    
    public class TrieNode {
        Map<Character, TrieNode> children;
        Queue<String> queue;
        public TrieNode() {
            this.children = new HashMap<Character, TrieNode>();
            this.queue = new PriorityQueue<>((a, b) -> b.toLowerCase().compareTo(a.toLowerCase()));
        }
    }

    class Solution
	{    
	    List<PairInt> list;
	    Map<Integer, Boolean> visited;
	    List<PairInt> criticalConnections(int numOfServers, int numOfConnections,
	                                      List<PairInt> connections)
	    {
	        Map<Integer, HashSet<Integer>> adj = new HashMap<>();
	        for(PairInt connection : connections){
	            int u = connection.first;
	            int v = connection.second;
	            if(adj.get(u) == null){
	                adj.put(u,new HashSet<Integer>());
	            }
	            adj.get(u).add(v);
	            if(adj.get(v) == null){
	                adj.put(v,new HashSet<Integer>());
	            }
	            adj.get(v).add(u);
	        }
	       
	        list = new ArrayList<>();
	        for(int i =0;i<numOfConnections;i++){
	            visited = new HashMap<>();
	            PairInt p = connections.get(i);
	            int x = p.first;
	            int y = p.second;
	            adj.get(x).remove(y);
	            adj.get(y).remove(x);
	            DFS(adj,1);
	            if(visited.size()!=numOfServers){
	                    if(p.first > p.second)
	                        list.add(new PairInt(p.second,p.first));
	                    else
	                        list.add(p);
	            }
	            adj.get(x).add(y);
	            adj.get(y).add(x);
	        }
	        return list;
	    }
	   
	    public void DFS(Map<Integer, HashSet<Integer>> adj, int u){
	        visited.put(u, true);
	        if(adj.get(u).size()!=0){
	            for(int v : adj.get(u)){
	                if(visited.getOrDefault(v, false)== false){
	                    DFS(adj,v);
	                }
	            }
	        }
	    }
	}

	//Articulation Point
	{	
		int time = 0;
		Map<Integer, HashSet<Integer>> adj = new HashMap<>();


        for(PairInt connection : connections){
            int u = connection.first;
            int v = connection.second;
            if(adj.get(u) == null){
                adj.put(u,new HashSet<Integer>());
            }
            adj.get(u).add(v);
            if(adj.get(v) == null){
                adj.put(v,new HashSet<Integer>());
            }
            adj.get(v).add(u);
        }

        // Mark all the vertices as not visited 
        boolean visited[] = new boolean[V]; 
        int disc[] = new int[V]; 
        int low[] = new int[V]; 
        int parent[] = new int[V]; 
        boolean ap[] = new boolean[V]; // To store articulation points 
  
        // Initialize parent and visited, and ap(articulation point) 
        // arrays 
        for (int i = 0; i < V; i++) 
        { 
            parent[i] = -1; 
            visited[i] = false; 
            ap[i] = false; 
        } 
  
        // Call the recursive helper function to find articulation 
        // points in DFS tree rooted with vertex 'i' 
        for (int i = 0; i < V; i++) 
            if (visited[i] == false) 
                APUtil(i, visited, disc, low, parent, ap); 
  
        // Now ap[] contains articulation points, print them 
        for (int i = 0; i < V; i++) 
            if (ap[i] == true) 
                System.out.print(i+" ");

///////////////////////////////////////////////////////////////////////
        void APUtil(int u, boolean visited[], int disc[], 
                int low[], int parent[], boolean ap[]) 
    	{ 
  
	        // Count of children in DFS Tree 
	        int children = 0; 
	  
	        // Mark the current node as visited 
	        visited[u] = true; 
	  
	        // Initialize discovery time and low value 
	        disc[u] = low[u] = ++time; 
	  
	        // Go through all vertices aadjacent to this 
	        
	        for(int v : adj.get(u))
	        {   
	            // If v is not visited yet, then make it a child of u 
	            // in DFS tree and recur for it 
	            if (!visited[v]) 
	            { 
	                children++; 
	                parent[v] = u; 
	                APUtil(v, visited, disc, low, parent, ap); 
	  
	                // Check if the subtree rooted with v has a connection to 
	                // one of the ancestors of u 
	                low[u]  = Math.min(low[u], low[v]); 
	  
	                // u is an articulation point in following cases 
	  
	                // (1) u is root of DFS tree and has two or more chilren. 
	                if (parent[u] == -1 && children > 1) 
	                    ap[u] = true; 
	  
	                // (2) If u is not root and low value of one of its child 
	                // is more than discovery value of u. 
	                if (parent[u] != -1 && low[v] >= disc[u]) 
	                    ap[u] = true; 
	            } 
	  
	            // Update low value of u for parent function calls. 
	            else if (v != parent[u]) 
	                low[u]  = Math.min(low[u], disc[v]); 
	        } 
    	}

	}
}






