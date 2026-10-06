import processing.core.PApplet;

public class Sketch extends PApplet { 
double ghostX_1 = 50;
double ghostX_2 = 50;
int ghostspeed = -1;
double batX = 100;
double batY = 100;
double batspeedX = 2;
double batspeedY = 2;
float batangle = 0;

double[] starX = new double[40];
double[] starY = new double[40];
float[] starspeed = new float[40];



    public void settings() {
        size(600, 600);

    } // end settings method

    public void setup() {
        for (int i = 0; i < 40; i++) {
            starX[i] = random(0, 600);
            starY[i] = random(10, 250);
            starspeed[i] = (float)random(0.2f, 0.8f);
        }
    } // end setup method

    public void draw() {

        background(31, 33, 46);
        drawRoad(0,350);
        drawBuilding(100,280);
        drawBuilding(50,280);
        drawBuilding(330,280);
        drawBuilding(360,280);
        drawBuilding(410,280);
        drawStore(200, 325, 5);
        drawStore(540, 325, 5);
        pumpkin(280, 333, 35, 30);
        drawGhost((int)ghostX_1, 350, 0.3f);
        if (frameCount % 120 == 0) {
            ghostX_1 = random(50, 550);
        }
        drawGhost((int)ghostX_2, 450, 0.3f);
        ghostX_2 += ghostspeed;
        if (ghostX_2 > 550 || ghostX_2 < 50) {
            ghostspeed *= -1;
        }


        for (int i = 0; i < 40; i++) {
            int starSize = (int)random(2, 5);
            drawStar((int)starX[i], (int)starY[i], starSize);
            starX[i] -= starspeed[i];
            if(starX[i] < 0) {
                starX[i] = 600;
                starY[i] = random(10, 250);
                starspeed[i] = (float)random(0.2f, 0.8f);
            }
        }

        drawBat((int)batX, (int)batY);
        batX += batspeedX;
        batY += batspeedY;
        if (batX > 550 || batX < 50) {
            batspeedX *= -1;
        }
        if (batY > 550 || batY < 0) {
            batspeedY *= -1;
        }
        drawMoon(500, 100, 80);
    } // end draw method
// Road
    public void drawRoad(int x, int y) {
        // Grass
        noStroke();
        fill(125, 170, 41);
        rect(x-100, y + 200 , 800, 50);

        push();
        fill(88, 88, 88);
        stroke(88, 88, 88);
        rect(x, y, 600, 200);

        fill(255, 255, 255);
        stroke(255, 255, 255);
        for (int i = 15; i < 600; i += 60) {
            line(x + i, y + 50, x + i + 30, y + 50);
            line(x + i, y + 150, x + i + 30, y + 150);
        }

        stroke(218,202,18);
        strokeWeight(3);
        line(x - 1, y + 100,x + 600, y + 100);
        pop();

        fill(155, 164, 163);
        rect(x, y, 600, 10);
    }


// Building
    public void drawBuilding(int x, int y) {     
        text(mouseX +" "+ mouseY, 10,10);     
        fill(50);     

        // main building     
        rect(x,y,30, 70);     
        fill(0,0,100);     

        // windows
        fill(255,255,0);
        rect(x+5,y+10,5,5);    
        rect(x+20,y+10,5,5);  
        rect(x+20,y+20,5,5);      
        rect(x+5,y+20,5,5);     
        rect(x+5,y+30,5,5);     
        rect(x+20,y+30,5,5);     

        fill(50);     
        //door     
        rect(x+10,y+60,5,10);
        rect(x+15,y+60,5,10);         
    }
// Store
    public void drawStore(int x, int y, int size) { 
        fill(143, 106, 90); 
        rect(x-6*size, y-5*size, 16*size, 10*size);

        //store 
        fill(212, 115, 91); 
        quad(x-7*size, y-5*size, x-6*size, y-10*size, x+10*size, y-10*size, x+11*size, y-5*size); 

        //roof 
        rect(x-5*size,y-3*size,4*size,7*size);
        //door 
        fill(0); circle(x-2*size, y, size/2); 
        fill(154, 164, 181); 
        rect(x,y-2*size,5*size, 3*size);

        //window 
        fill(190, 152, 40); 
        rect(x-size/2, y+size, 6*size, size);
    }
// Pumpkin
    public void pumpkin(int x, int y, int width, int height) {     
        drawStem(x, y, width, height);     
        drawBody(x, y, width, height);   
    } // end pumpkin method    

    public void drawBody(int x, int y, int Bwidth, int Bheight) {     
        fill(255, 165, 0);     
        stroke(205, 115, 0);     
        Bwidth = (int) (Bwidth / 2);     
        ellipse((int) (x - Bwidth / .75) + (Bwidth / 3),y,Bwidth,Bheight);     
        ellipse((int) (x - Bwidth / 2) + (Bwidth / 5),y,Bwidth,Bheight);     
        ellipse((int) (x + Bwidth / 2) - (Bwidth / 5),y,Bwidth,Bheight);     
        ellipse((int) (x + Bwidth / .75) - (Bwidth / 3),y,Bwidth,Bheight);    
        stroke(0);   
    } // end drawBody method      

    public void drawStem(int x, int y, int Swidth, int Sheight) {     
        fill(173, 226, 135);     
        rect((int) (x - Swidth/5.0), (int) (y-Sheight/1.4), Swidth/3, (int)(Sheight/2.5), 28);   
    }// end drawStem method

// Ghost
    public void drawGhost(int cx, int cy, float size) {      
        push();
        translate(cx, cy);
        scale(size);
        drawBody(0, 0);         
        drawEyes(20, -25);         
        drawEyes(-20, -25);        
        drawMouth(0, 25);  
        pop();
    }      

    public void drawEyes(int cx, int cy) {         
        fill(0);         
        ellipse(cx, cy, 30, 15);         
        ellipse(cx, cy, 30, 15);         
    }     

    public void drawMouth(int cx, int cy) {         
        fill(0);         
        ellipse(cx,cy,100,50);         
    }     

    public void drawBody(int cx, int cy) {         
        fill(255);         
        strokeWeight(0);         
        arc(cx, cy+100, 200, 500, radians(180), radians(360), OPEN);        
        triangle(cx-100, cy+100, cx-50, cy+100, cx-75, cy+175);         
        triangle(cx, cy+100, cx-50, cy+100, cx-25, cy+175);         
        triangle(cx, cy+100, cx+50, cy+100, cx+25, cy+175);         
        triangle(cx+50, cy+100, cx+100, cy+100, cx+75, cy+175);        
    }

//Bat
    public void drawBat(int x, int y) {
        push();
        translate(x, y);
        rotate(batangle);
        drawBody1(0,0);     
        drawHead(0,0);     
        drawEye(0,-65);     
        drawEar(0,0);         
        drawWing(0,0);     
        drawFeet(0,0);
        pop();
        batangle += 0.5;

     
    }   

    public void drawBody1(int x, int y) {      
        fill(134, 119, 95);   
        ellipse(x,y,60,90);   
    }   

    public void drawHead(int x, int y) {     
        fill(210, 180, 140);     
        circle(x,y-60,50);     
        fill(71, 52, 52);     
        circle(x,y-55,10);     
        fill(255);     
        triangle(x-8,y-45,x-1,y-45,x-5,y-36);     
        triangle(x+1,y-45,x+8,y-45,x+5,y-36);   
    }   

    public void drawEye(int x, int y) {    
        fill(101, 67, 33);    
        ellipse(x-10,y,10,15);    
        ellipse(x+10,y,10,15);  
    }   

    public void drawEar(int x, int y) {     
        fill(101, 67, 33);     
        triangle(x-25,y-70,x-15,y-105,x-5,y-80);     
        line(x-23,y-80,x-7,y-80);     
        line(x-21,y-88,x-10,y-88);     
        triangle(x+25,y-70,x+15,y-105,x+5,y-80);     
        line(x+7,y-80,x+23,y-80);     
        line(x+10,y-88,x+21,y-88);   
    }   

    public void drawFeet(int x, int y) {     
        fill(29,2,0);    
        rect(x-15,y+40,4,25);     
        line(x-13,y+65,x-23,y+73);     
        line(x-13,y+65,x-18,y+75);     
        line(x-13,y+65,x-13,y+76);     
        line(x-13,y+65,x-8,y+75);     
        line(x-13,y+65,x-3,y+73);     
        rect(x+11,y+40,4,25);     
        line(x+13,y+65,x+3,y+73);     
        line(x+13,y+65,x+8,y+75);     
        line(x+13,y+65,x+13,y+76);     
        line(x+13,y+65,x+18,y+75);     
    line(x+13,y+65,x+23,y+73);   
    }   

    public void drawWing(int x, int y) {   
        fill(75,47,24);   
        arc(x-30,y-35,140,100,0,HALF_PI);   
        arc(x+30,y-35,140,100,HALF_PI,PI);   
    }

    public void drawMoon(int x, int y, int size) {
        noStroke();
        fill(255, 240, 180);
        circle(x, y, size);
        fill(31,33,46);
        circle(x - size/3, y - size/5, size);
    }

    public void drawStar(int x, int y, int size) {
        fill(255,255,200);
        noStroke();
        circle(x, y, size);
    }


} // end Sketch class