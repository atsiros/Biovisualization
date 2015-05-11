import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class Tsiros_1 extends PApplet {

int[][] cells;
int[][] cellsState;

// Color variables
int alive = color(255,255,255);
int prey = color(0,255,0);
int predator = color(255,0,0);

// Timer variables
int period = 300;
int time = 0;

// Pause
boolean pause = false;

// Set up
// State of cells for randomly assigned first generation

public void setup() {
  size (640, 360);
  
  // background color
  background(0);
  
  // gray gridlines
  stroke(50);
  
  cells = new int[width/5][height/5];
  cellsState = new int[width/5][height/5];
  
  //
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
      cells[x][y] = PApplet.parseInt(state); // define state for each cell, prey and predators
    }
  }
}

public void draw() {
  
  // Place first generation cells
  for (int x = 0; x < width/5; x++) {
    for (int y = 0; y < height/5; y++) {
      if (cells[x][y] == 1) {
        fill(alive);
      }
      if (cells[x][y] == 2) {
        fill(predator);
      }
      if (cells[x][y] == 3) {
        fill(prey);
      }
      if (cells[x][y] == 0) {
        fill(0);
      }
      
      // Draw grid
      rect (x*5, y*5, 5, 5);
    }
  }
  
  // Timer iteration
  if (millis() - time > period) {
    clock();
    time = millis();
  }
}


public void clock() {
  
  // As clock ticks, update cellStates
  for (int x = 0; x < width/5; x++) {
    for (int y = 0; y < height/5; y++) {
      cellsState[x][y] = cells[x][y];
    }
  }
  
  // Determine neighbors for each cell
  for (int x = 0; x < width/5; x++) {
    for (int y = 0; y < height/5; y++) {
      int cellNeighbors = 0; // begin neighbor counter at zero
      int predNeighbors = 0;
      int preyNeighbors = 0;
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
        if (cellNeighbors < 2 || cellNeighbors > 3) {
          cells[x][y] = 0; // 
        }
        if (predNeighbors > 1) {
          cells[x][y] = 0;
        }
        if (preyNeighbors > 1) {
          cells[x][y] = 1;
        }
      }
      if (cellsState[x][y] == 2) {
        if (cellNeighbors > 1) {
          cells[x][y] = 1;
        }
        if (preyNeighbors > 0) {
          cells[x][y] = 1;
        }
      }
      if (cellsState[x][y] == 3) {
        if (cellNeighbors > 1) {
          cells[x][y] = 0;
        }
        if (predNeighbors > 0) {
          cells[x][y] = 0;
        }
      }
      if (cellsState[x][y] == 0) {
        if ((cellNeighbors == 3) && (predNeighbors == 0)) {
          cells[x][y] = 1; //
        }
      }
    }
  }
}

public void keyPressed() {
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
        cells[x][y] = PApplet.parseInt(state); // define state for each cell, prey and predators
      }
    }
  }
}
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "Tsiros_1" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
