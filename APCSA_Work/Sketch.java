import processing.core.PApplet;

public class Sketch extends PApplet {
    int x = 300;
    int y = 350;
    // color
    int r = 150;
    int g = 210;
    int b = 250;
    int SkinColor = color(249, 223, 196);



    public void settings() {
        size(600, 600);
    }

    public void setup() {
        background(220);
    }

    public void keyPressed() {
        if (key == CODED) {
            if (keyCode == LEFT) {
                x -= 10;
            } else if (keyCode == RIGHT) {
                x += 10;
            } else if (keyCode == UP) {
                y -= 10;
            } else if (keyCode == DOWN) {
                y += 10;
            }
        }
    }

    public void draw() {
        //background
        //sky
        background(r, g, b);

        //Far Grass
        noStroke();
        fill(145, 200, 120);
        ellipse(100, 500 ,600, 200);
        ellipse(500, 500 ,600, 250);

        //front Grass
        fill(100, 180, 80);
        ellipse(100, 570 ,660, 200);
        ellipse(500, 570 ,660, 250);





        textSize(18);
        fill(255, 0, 0);
        strokeWeight(1);
        stroke(0, 0, 0);
        text(x + " " + y, 50, 50);
        // center(310,255)


        // antenna
        fill(SkinColor);
        //triangle(310, 40, 270, 95, 350, 95);
        triangle(x, y - 215, x - 40, y - 160, x + 40, y - 160);


        // head
        fill(SkinColor);
        ellipse(x, y - 90, 200, 150);

        // left ear
        noStroke();
        fill(0xFFFFD4A9);
        ellipse(x - 100, y - 90, 30, 50);
        fill(0xFF854e27);
        ellipse(x - 110, y - 90, 20, 40);
        fill(0xFF644030);
        ellipse(x - 120, y - 90, 15, 30);
        // right ear
        fill(0xFFFFD4A9);
        ellipse(x + 100, y - 90, 30, 50);
        fill(0xFF854e27);
        ellipse(x + 110, y - 90, 20, 40);
        fill(0xFF644030);
        ellipse(x + 120, y - 90, 15, 30);

        // left leg
        stroke(0 ,0 ,0);
        fill(SkinColor);
        rect(x - 40, y + 85, 25, 60);
        // right leg
        rect(x + 15, y + 85, 25, 60);

        // Body
        fill(SkinColor);
        rect(x - 60, y - 30, 120, 125, 0, 0, 30, 30);

        // feet
        stroke(0, 0, 0);
        rect(x - 55, y + 135, 43, 25, 30, 0, 0, 2);
        rect(x + 12, y + 135, 43, 25, 0, 30, 2, 0);

        // arm
        fill(SkinColor);
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
        fill(SkinColor);
        arc(x + 1, y - 85, 30, 20, 0, PI);

        // duzi
        fill(0xFFebd6cb);
        ellipse(x, y + 25, 90, 100);

        // pocket
        fill(255, 0, 0);
        rect(x - 30, y + 25, 60, 30);

        // 
        fill(SkinColor);
        square(x-90 ,y - 30, 30);
        square(x+60, y -30, 30);

        // button (center)
        fill(0xFFEFEFFF);
        strokeWeight(3);
        circle(x, y, 20);

        

        // x++;
        /*
        if (x >= width + 150) {
            x = -100;
        } else if (x < -150) {
            x = width + 100;;
        }
        */
        // y = -165 and 795,x = -130 and 730
        if (x <= -130 || x >= width + 130 || y <= -165 || y >= width + 195) {
            x = 300;
            y = 350;
            for (int i = 0; i < 2; i++) {
                SkinColor = color(255);
                SkinColor = color(249, 223, 196);
            }

        }


        // IO.println(r + " " + g + " " + b);


        


    }



}