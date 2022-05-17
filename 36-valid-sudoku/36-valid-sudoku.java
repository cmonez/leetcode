class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<String> occurs = new HashSet<String>();
        
        for(int i = 0; i < 9; i++) {
            for(int j = 0; j < 9; j++) {
                if(board[i][j] != '.') {
                    if(occurs.contains("row" + i + board[i][j]) || occurs.contains("col" + j + board[i][j])) {
                        return false;
                    }
                    occurs.add("row" + i + board[i][j]);
                    occurs.add("col" + j + board[i][j]);
                    if(occurs.contains("square" + (i/3) * 3 + j/3 + board[i][j])) {
                        return false;
                    }
                    occurs.add("square" + (i/3) * 3 + j/3 + board[i][j]);                       
                }
            }
        }
        return true;
    }
}