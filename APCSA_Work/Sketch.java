import processing.core.PApplet;

public class Sketch extends PApplet {

    public void settings() {
        size(600, 600);
        
    }

    public void setup() {
        background(220);
        
    }

    public void draw() {
        background(220);
        textSize(18);
        fill(255, 0, 0);
        text(mouseX + " " + mouseY, 50, 50);
        // antenna
        fill(0xFFf9dfc4);
        triangle(310, 40, 270, 95, 350, 95);

        // head
        fill(0xFFf9dfc4);
        ellipse(310, 165, 200, 150);

        // ear
        fill(0xFFf9dfc4);
        ellipse(210, 165, 30, 50);
        ellipse(410, 165, 30, 80);

        ellipse(200, 165, 20, 40);

        // left leg
        fill(0xFFf9dfc4);
        rect(270, 340, 25, 60);
        // right leg
        rect(325, 340, 25, 60);

        // Body
        fill(0xFFf9dfc4);
        rect(250, 225, 120, 125, 0, 0, 30, 30);

        // feet
        rect(255, 390, 43, 25, 30, 0, 0, 2);
        rect(322, 390, 43, 25, 0, 30, 2, 0);

        // arm
        ellipse(243, 270, 25, 80);
        circle(243, 310, 30);

        ellipse(377, 270, 25, 80);
        circle(377, 310, 30);

        //eyes
        fill(0xFFae7145);
        circle(275, 140, 30);
        circle(345, 140, 30);
        fill(0xFFeedbcd);
        circle(275, 140, 20);
        circle(345, 140, 20);
        fill(0x000000);
        circle(275, 140, 15);
        circle(345, 140, 15);
        fill(0xFFFFFFFF);
        circle(277, 138, 5);
        circle(347, 138, 5);
        // nose
        fill(0xFFdbba91);
        circle(310, 140, 20);

        // mouth
        fill(0xFFf9dfc4);
        arc(311, 170, 30, 20, 0, PI);

        // duzi
        fill(0xFFebd6cb);
        ellipse(310, 285, 90, 100);

        // button




    }

}