class EmptyGrid {

    constructor(sizeX, sizeY){
        this.grid = new Array(sizeY);
        for (let i = 0; i < this.grid.length; i++){
            this.grid[i] = new Array(sizeX).fill(`_`);
        }
        this.Rwin = '';
        this.Ywin = '';
        this.regR = new RegExp('[R+]{4,}');
        this.regY = new RegExp('[Y+]{4,}');
    }

    printGrid = function(){
        console.log(this.grid)
    }

    prettyPrintGrid = function(){
        for (let i = 0; i < this.grid.length; i++){
            let array = '';
            for (let j = 0; j < this.grid[0].length; j++){
                array+= (j == 0)? `|${this.grid[i][j]}|` : `${this.grid[i][j]}|`;
            }console.log(array)
        }
        console.log('')
    }
}

class Grid extends EmptyGrid{

    constructor(sizeX, sizeY){
        super(sizeX, sizeY);
    }

    checkLignsWin = function(grid){
        for (let lign of grid){
            this.Rwin = this.regR.test(lign);
            this.Ywin = this.regY.test(lign);
            if (this.Rwin) { console.log('Red wins');}
            else if (this.Ywin) { console.log('Yellow wins')}
        } return false
    }

    reverseGrid = function(){

        let turned_grid = new Array(this.grid[0].length);
            
        for (let i = 0; i < this.grid[0].length; i++){
            turned_grid[i] = new Array(this.grid.length);
            for (let j = 0; j < this.grid.length; j++){
                turned_grid[i][j] = this.grid[j][i];
            }
        }
        return turned_grid
    }

    getDiagoGrid = function(){

        let diagoGrid1 = new Array(this.grid.length + this.grid[0].length - 7), // 7 -> x.size+y.size - 1 - (minimum size of diago -1)*2
            diagoGrid2 = new Array(this.grid.length + this.grid[0].length - 7)

        for (let k = 3-this.grid.length; k < this.grid.length - 2; k++){
            let Diag1 = '',
                Diag2 = '';
            for (let col = 0; col < grid[0].length; col++){
                for (let row = 0; row < grid.length; row++){
                    if (row == col - k && k> 3-this.grid.length)
                        { Diag1 += this.grid[row][col] }
                    if (row == this.grid.length - (1 + col + k) && k< this.grid.length -3)
                        { Diag2 += this.grid[row][col] }
                }
            }
            if (k > 3 - this.grid.length) diagoGrid1[k+2] = Diag1 
            if (k < this.grid.length - 3) diagoGrid2[k+3] = Diag2 
    }
    return {'diagoGrid1' : diagoGrid1, 'diagoGrid2' : diagoGrid2 }
}
    checkRowWin = function(){
        this.checkLignsWin(this.grid)
    }
    checkColWin = function(){
        let returned = this.reverseGrid()
        return this.checkLignsWin(returned)
    }
    checkDiag1Win = function(){
        let diag1 = this.getDiagoGrid().diagoGrid1;
        return this.checkLignsWin(diag1);
    }
    checkDiag2Win = function(){
        let diag2 = this.getDiagoGrid().diagoGrid2;
        return this.checkLignsWin(diag2);
    }
    checkDiagWin = function() {
        return (this.checkDiag1Win())? this.checkDiag1Win() : this.checkDiag2Win()
    }
    
    
    firstEmpty = function(x){ // En fait cest first empty d'une ligne du coup class Lign ??
        let turned = this.reverseGrid()
        for (let i = turned[x].length-1; i >= 0; i --){
            if (turned[x][i] != 'R' && turned[x][i] != 'Y') return i
        }
    }

    addToken = function(Token, x){
        let y = this.firstEmpty(x)
        // let color = Token.color,
            // token = (color == 'red')? 'R' : 'Y',
        this.grid[x][y] = Token.color // petite animation ?
    };

}


let grid = [
    ['-', '-', '-', '-', '-', '-', '-'],
    ['-', 'Y', '-', 'b', 'b', 'b', 'b'],
    ['-', 'c', 'R', 'x', 'x', 'x', 'x'],
    ['-', 'c', 'x', 'R', 'x', 'x', 'x'],
    ['-', 'c', 'x', 'x', 'R', 'x', 'x'],
    ['-', 'c', 'x', 'x', 'x', 'x', 'x']
]

class Token {
    constructor(color){
        this.color = color
    }
    // c'est tout?
}

const SIZE_X = 7,
      SIZE_Y = 6;

game = new Grid(SIZE_X, SIZE_Y)
// game_grid.prettyPrintGrid()
game.grid = grid
game.firstEmpty(3)
// console.log(t, 'red')
// game_grid.prettyPrintGrid()
// ret = game_grid.reverseGrid()
// game_grid.grid = ret

// game_grid.prettyPrintGrid()
// game_grid.grid = game_grid.reverseGrid()
// game_grid.prettyPrintGrid()
// console.log(ret)


while (!game.checkColWin() && !game.checkDiagWin() && !game.checkRowWin()){  // Game Loop
    console.log('ici le jeu')
       x = stderr.input("please select a token ('R' / 'Y') :") // input à check
       jeton = new Token(x)

    // ça joue
    //  
}

