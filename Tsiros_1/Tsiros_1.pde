// Color variables
color alive = color(255,255,255); // white
color prey = color(0,255,0); // green
color predator = color(255,0,0); // red

// Timer variables
int period = 300;
int time = 0;

int[][] cells;
int[][] cellsState;

// Pause
boolean pause = false;

// Set up
// State of cells for randomly assigned first generation

void setup() {
  size (640, 360);
  
  // background color
  background(0);
  
  // gray gridlines
  stroke(50);
  
  cells = new int[width/5][height/5];
  cellsState = new int[width/5][height/5];
  
  //
  for (int x = 0; x < width/5; x++) {
    for (int y = 0; y < height/5; y++) {
      float state = random (100); // randomly assigning first generation
      if (state < 4) { // probability of cell state being "prey"
        state = 3;
      }
      if ((state > 3) && (state < 7)) { // probability of cell state being "predator"
        state = 2;
      }
      if ((state > 6) && (state < 31)) { // probability of cell state being "alive"
        state = 1;
      }
      if (state > 30) { // probability of cell state being "dead"
        state = 0;
      }
      cells[x][y] = int(state); // define state for each cell, prey and predators
    }
  }
}

void draw() {
  
  // Place first generation cells
  for (int x = 0; x < width/5; x++) {
    for (int y = 0; y < height/5; y++) {
      if (cells[x][y] == 1) { // alive
        fill(alive);
      }
      if (cells[x][y] == 2) { // predator
        fill(predator);
      }
      if (cells[x][y] == 3) { // prey
        fill(prey);
      }
      if (cells[x][y] == 0) { // dead
        fill(0);
      }
      
      // Draw grid
      rect (x*5, y*5, 5, 5);
    }
  }
  
  // Timer iteration
  if (millis() - time > period) {
    if (!pause) {
      clock();
      time = millis();
    }
  }
  
  else if (pause) {
    for (int x = 0; x < width/5; x++) {
      for (int y = 0; y < height/5; y++) {
        cellsState[x][y] = cells[x][y];
      }
    }
  }
}

void clock() {
  // As clock ticks, update cellStates for working copy
  for (int x = 0; x < width/5; x++) {
    for (int y = 0; y < height/5; y++) {
      cellsState[x][y] = cells[x][y];
    }
  }
  
  // Determine neighbors for each cell
  for (int x = 0; x < width/5; x++) {
    for (int y = 0; y < height/5; y++) {
      int cellNeighbors = 0; // begin neighbor counter at zero
      int predNeighbors = 0; // predator neighbor counter
      int preyNeighbors = 0; // prey neighbor counter
      for (int x1 = x-1; x1 <= x + 1; x1++) { // accounts for left and right neighbors
        for (int y1 = y-1; y1 <= y + 1; y1++) { // accounts for all below and above neighbors
          if (((x1 >= 0) && (x1 < width/5)) && ((y1 >= 0) && (y1 < height/5))) {
            if (!((x1 == x) && (y1 == y))) { // check against self
              if (cellsState[x1][y1] == 1) { // if this specific neighbor is alive
                cellNeighbors ++; // update neighbor counter
              }
              if (cellsState[x1][y1] == 2) {
                predNeighbors ++;
              }
              if (cellsState[x1][y1] == 3) {
                preyNeighbors ++;
              }
            }
          }
        }
      }
        
      // Rules
      if (cellsState[x][y] == 1) { // if the cell is alive
        if (cellNeighbors < 2 || cellNeighbors > 3) { // unless cell has 2 or 3 neighbors
          cells[x][y] = 0; // kill
        }
        if (predNeighbors > 1) { // if cell has 2 or more predator neighbors, kill
          cells[x][y] = 0;
        }
        if (preyNeighbors > 1) { // if cell has 2 or more predator neighbors, birth
          cells[x][y] = 1;
        }
      }
      if (cellsState[x][y] == 2) { // if cell is a predator
        if (cellNeighbors > 1) { // if predator has 2 or more cell neighbors
          cells[x][y] = 1; // keep alive
        }
        if (preyNeighbors > 0) { // if predator has 1 or more prey neihgbors
          cells[x][y] = 1; // keep alive
        }
      }
      if (cellsState[x][y] == 3) { // if cell is prey
        if (cellNeighbors > 1) { // if prey has 2 or more cell neighbors
          cells[x][y] = 0; // kill
        }
        if (predNeighbors > 0) { // if prey has 1 or more predator neighbors
          cells[x][y] = 0; // kill
        }
      }
      if (cellsState[x][y] == 0) { // if cell dead
        if ((cellNeighbors == 3) && (predNeighbors == 0)) { // if cell has 3 cell neighbors and 0 predator neighbors
          cells[x][y] = 1; // birth
        }
      }
    }
  }
}

// Press 'r' or 'R' on keyboard to reset to inital settings
void keyPressed() {
  if (key == 'r' || key == 'R') {
    for (int x = 0; x < width/5; x++) { // while x is less than 128 to fit max # of cells in width of frame
      for (int y = 0; y < height/5; y++) { // while y is less than 128
        float state = random (100); // randomly assigning first generation
        //print (" ", state);
        if (state < 4) { // probability of cell state beginning "dead" 75%
          state = 3;
        }
        if ((state > 3) && (state < 7)) { // probability of prey being alive 5%
          state = 2;
        }
        if ((state > 6) && (state < 31)) { // probability of predators being alive 5%
          state = 1;
        }
        if (state > 30) { // probability of cells being alive
          state = 0;
        }
        cells[x][y] = int(state); // define state for each cell, prey and predators
      }
    }
  }
  if (key == ' ') {
    pause = !pause;
  }
}
