import java.util.ArrayList; 
import java.util.Collections; 

public class MoveChooser {
 
        
    public static final int[][] SCORES_OF_SQUARES = { 
        { 120, -20, 20, 5, 5, 20, -20, 120 }, 
        { -20, -40, -5, -5, -5, -5, -40, -20 },
        { 20, -5, 15, 3, 3, 15, -5, 20 }, 
        { 5, -5, 3, 3, 3, 3, -5, 5 }, 
        { 5, -5, 3, 3, 3, 3, -5, 5 },
        { 20, -5, 15, 3, 3, 15, -5, 20 }, 
        { -20, -40, -5, -5, -5, -5, -40, -20 },
        { 120, -20, 20, 5, 5, 20, -20, 120 } 
    };

    private static final int MAXIMUM = Integer.MAX_VALUE;
    private static final int MINIMUM = Integer.MIN_VALUE; 
  
    public static Move chooseMove(BoardState boardState){

	int searchDepth= Othello.searchDepth;

        ArrayList<Move> moves= boardState.getLegalMoves();
        ArrayList<Integer> results = new ArrayList<Integer>();
        // Computing the children nodes
        ArrayList<BoardState> children = new ArrayList<>();
        if(moves.isEmpty()){
            return null;
	}
       
        // Making the AI move and getting the next possible states
        for (Move move : moves) {
            BoardState boardCopy = boardState.deepCopy();
            boardCopy.makeLegalMove(move.x, move.y);
            children.add(boardCopy);
        }
         // The maximizing node as the function is only called when it is AI turn
        for (BoardState child : children) {
            results.add(minimaxAlphaBetaPruning(child, searchDepth - 1, MINIMUM, MAXIMUM));
        }

        // Returning the move for maximum result
        int maximum = Collections.max(results);
        return moves.get(results.indexOf(maximum));

        
    }
    public static int minimaxAlphaBetaPruning(BoardState board, int depth, int alpha, int beta) {

        ArrayList<Move> moves = board.getLegalMoves();
        ArrayList<BoardState> children = new ArrayList<>();

        if (!moves.isEmpty()) {
            for (Move move : moves) {
                BoardState boardCopy = board.deepCopy();
                boardCopy.makeLegalMove(move.x, move.y);
                children.add(boardCopy);
            }
        } 
        else {
            // If no moves availabe, turn is passed to the other player.
            BoardState boardCopy = board.deepCopy();
            boardCopy.colour = -boardCopy.colour;
            children.add(boardCopy);
        }

        if (depth == 0 || board.gameOver()) {
            return evaluate(board);
        }

        if (board.colour == 1) {
            // The maximizing node
            alpha = MINIMUM;
            for (BoardState child : children) {
                 
                alpha = Math.max(alpha, minimaxAlphaBetaPruning(child, depth - 1, alpha, beta));
                
                if (alpha >= beta) {
                    break;
                }
            }
            
            return alpha;
        } 
        else {
            // The minimizing node
            beta = MAXIMUM;
            for (BoardState child : children) {
                 
                beta = Math.min(beta, minimaxAlphaBetaPruning(child, depth - 1, alpha, beta));
             
                if (alpha >= beta) {
                    break;
                }
            }
             
            return beta;
        }
    }

    // Static evaluation function
    public static int evaluate(BoardState boardState) {
        int score = 0;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
             
                if (boardState.getContents(i, j) == 1) {
                    score += SCORES_OF_SQUARES[i][j];
                }
                if (boardState.getContents(i, j) == -1) {
                    score -= SCORES_OF_SQUARES[i][j];
                }
            }
        }
        return score;
    }
}
