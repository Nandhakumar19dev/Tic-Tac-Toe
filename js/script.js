console.log("it is working");
var player = "X";
// const buttons = document.getElementsByTagName("button");
const board = document.getElementsByClassName("container")[0]; 
const buttons = [...board.getElementsByTagName('button')];

win_map = {
  1:[[2, 3], [4, 7], [5, 9]], 
  2:[[1, 3], [5, 8]],
  3:[[1, 2], [6, 9], [5, 7]],
  4:[[1, 7], [5, 6]],
  5:[[4, 6], [1, 9], [2, 8], [3, 7]],
  6:[[4, 5], [3, 9]],
  7:[[1, 4], [8, 9], [3, 5]],
  8:[[7, 9], [2, 5]],
  9:[[1, 5], [7, 8], [3, 6]]
}

buttons.forEach(button => {
  button.addEventListener('click', function handleClick(event) {
    button.textContent = player;
    // button.setAttribute("style.color", "red");
    button.style.backgroundColor = "#9aadad";
    is_game_over(button.value, player);
    player = player=="X"?"O":"X";
    
  });
});


function is_game_over(value, current_cell_tc) {
  clicked_cell_win_checks = win_map[value];
  clicked_cell_win_checks.forEach(values=>{
    function checkAllSame(value) {
      button = buttons[value-1];
      return current_cell_tc == button.textContent;
    }
    if (values.every(checkAllSame)){
      info = document.getElementById("info");
      info.textContent = `${current_cell_tc} Wins`;
      info.style.display = "initial";
      buttons[value-1].style.backgroundColor = "#5bc0de";
      values.forEach(value=>{
        button = buttons[value-1];
        button.style.backgroundColor = "#5bc0de";
      })
        }  }
  )
} 


reset_buttons = [...document.getElementsByClassName("reset")];

reset_buttons.forEach(reset_button=>{
    reset_button.addEventListener('click', 
                             function handleEvent(event){
    console.log("reset button click OK...");
    buttons.forEach(button=>{
      button.style.backgroundColor = "#1d3b3a";
      button.textContent= "";
      
    }
                   );
  player = "X";
  info = document.getElementById("info");
  // info.textContent = `${current_cell_tc} Wins`;
  info.style.display = "none";
      })
                                                      
})