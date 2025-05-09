/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    var isEveryRowValid = function(board){
        for(let row of board){
           let dict={};
           for(let cell of row){
            if(cell=='.')continue;
            if(dict[cell]){
                return false;
            }else{
                dict[cell]=1;
            }
           } 
        }
        return true;
    }
    var isEveryColValid = function(board){
        for(let col=0;col<9;col++){
           let dict={};
           for(let row=0;row<9;row++){
            let cell=board[row][col];
            if(cell=='.')continue;
            if(dict[cell]){
                return false;
            }else{
                dict[cell]=1;
            }
           } 
        }
        return true;
    }
    var isEveryBoxValid = function(board){
        let subBoxes = [];
        for(let boxRow=0;boxRow<9;boxRow+=3){
            for(let boxCol=0;boxCol<9;boxCol+=3){
                let dict={};
                for(let row=0;row<3;row++){
                    for(let col=0;col<3;col++){
                        let cell = board[boxRow+row][boxCol+col];
                        if(cell=='.') continue;
                        if(dict[cell]){
                            return false;
                        }
                        dict[cell]=1;
                    }
                }
            }
        }
        return true;
    }
    return (isEveryRowValid(board) && isEveryColValid(board) && isEveryBoxValid(board))
};
