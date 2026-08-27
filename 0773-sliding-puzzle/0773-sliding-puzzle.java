class Solution {

    public int slidingPuzzle(int[][] board) {
        StringBuilder sb = new StringBuilder();

        for (int[] row : board) {
            for (int num : row) {
                sb.append(num);
            }
        }

        String start = sb.toString();
        String target = "123450";

        int[][] neighbors = {
            {1, 3},
            {0, 2, 4},
            {1, 5},
            {0, 4},
            {1, 3, 5},
            {2, 4}
        };

        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.offer(start);
        visited.add(start);

        int moves = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                String current = queue.poll();

                if (current.equals(target)) {
                    return moves;
                }

                int zeroIndex = current.indexOf('0');

                for (int next : neighbors[zeroIndex]) {
                    char[] arr = current.toCharArray();

                    char temp = arr[zeroIndex];
                    arr[zeroIndex] = arr[next];
                    arr[next] = temp;

                    String newState = new String(arr);

                    if (!visited.contains(newState)) {
                        visited.add(newState);
                        queue.offer(newState);
                    }
                }
            }

            moves++;
        }

        return -1;
    }
}