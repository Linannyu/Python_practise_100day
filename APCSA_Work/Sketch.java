import processing.core.PApplet;

public class Sketch extends PApplet {

    public void settings() {
        size(600, 600);
        
    }

    public void setup() {
        background(220);
        
    }

    public void draw() {
        int x = mouseX;
        int y = mouseY;

        background(220);
        textSize(18);
        fill(255, 0, 0);
        strokeWeight(1);
        stroke(0, 0, 0);
        text(x + " " + y, 50, 50);
        // antenna
        fill(0xFFf9dfc4);
        triangle(310, 40, 270, 95, 350, 95);


        // head
        fill(0xFFf9dfc4);
        ellipse(310, 165, 200, 150);

        // left ear
        noStroke();
        fill(0xFFFFD4A9);
        ellipse(210, 165, 30, 50);
        fill(0xFF854e27);
        ellipse(200, 165, 20, 40);
        fill(0xFF644030);
        ellipse(190, 165, 15, 30);
        // right ear
        fill(0xFFFFD4A9);
        ellipse(410, 165, 30, 50);
        fill(0xFF854e27);
        ellipse(420, 165, 20, 40);
        fill(0xFF644030);
        ellipse(430, 165, 15, 30);

        // left leg
        stroke(0 ,0 ,0);
        fill(0xFFf9dfc4);
        rect(270, 340, 25, 60);
        // right leg
        rect(325, 340, 25, 60);

        // Body
        fill(0xFFf9dfc4);
        rect(250, 225, 120, 125, 0, 0, 30, 30);

        // feet
        stroke(0, 0, 0);
        rect(255, 390, 43, 25, 30, 0, 0, 2);
        rect(322, 390, 43, 25, 0, 30, 2, 0);

        // arm
        fill(0xFFf9dfc4);
        ellipse(x - 75, y + 15, 25, 80);
        ellipse(x + 75, y + 15, 25, 80);

        fill(0xFFFFFFFF);
        circle(x + 76, y + 55, 30);
        circle(x - 75, y + 55, 30);

        //eyes
        strokeWeight(1);
        fill(0xFFae7145);
        circle(x - 35, y - 115, 30);
        circle(x + 35, y - 115, 30);
        fill(0xFFeedbcd);
        circle(x - 35, y - 115, 20);
        circle(x + 35, y - 115, 20);
        fill(0x000000);
        circle(x - 35, y - 115, 15);
        circle(x + 35, y - 115, 15);
        fill(0xFFFFFFFF);
        circle(x - 33, y - 117, 5);
        circle(x + 37, y - 117, 5);

        // nose
        fill(0xFFdbba91);
        circle(x, y - 115, 20);

        // mouth
        fill(0xFFf9dfc4);
        arc(x + 1, y - 85, 30, 20, 0, PI);

        // duzi
        fill(0xFFebd6cb);
        ellipse(x, y + 25, 90, 100);

        // pocket
        fill(255, 0, 0);
        rect(x - 30, y + 25, 60, 30);

        // 
        fill(0xFFf9dfc4);
        square(x-90 ,y - 30, 30);
        square(x+60, y -30, 30);

        // button (center)
        fill(0xFFEFEFFF);
        strokeWeight(3);
        circle(x, y, 20);

        // center(310,255)
    



    }

}