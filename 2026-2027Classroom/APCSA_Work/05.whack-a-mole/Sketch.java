import processing.core.PApplet;

public class Sketch extends PApplet {
    int molesize;
    int x,y;
    int r,g,b;

    public void settings() {
        size(600, 600);
    }

    public void setup() {
        spawnTarget();
        molesize = 50;
        // if (frameCount % 30 == 0) {
        //     x = (int)(Math.random() * 600);
        //     y = (int)(Math.random() * 600);
        // }

    }

    public void draw() {
        background(7, 166, 240);
        fill(255);
        circle(x, y, molesize);
        text(mouseX + " " + mouseY,100,100);
    }

    public void mousePressed() {
        if ((int)(Math.random() * 10) > 2) {
            IO.println("click");
        } else {
            IO.println("ouch!");
        }
        IO.println(x);
        calculateDistance(mouseX, mouseY, x, y);
        spawnTarget();

    }

    public void spawnTarget() {
        molesize = (int)((Math.random() * 41) + 50);
        r = (int)(Math.random() * 255);
        g = (int)(Math.random() * 255);
        b = (int)(Math.random() * 255);
        x = (int)(Math.random() * 600);
        y = (int)(Math.random() * 600);
    }

    public double calculateDistance(int x1, int y1, int x2, int y2) {
        IO.println("mouseX is " + x1);
        IO.println("mousey is " + y1);
        IO.println("center_x is " + x2);
        IO.println("center_y is " + y2);
        IO.println(x2 - x1 + " " + Math.pow(x2 - x1, 2));
        IO.println(y2 - y1 + " " + Math.pow(y2 - y1, 2));

        double sum = Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2);
        double sqrt = Math.sqrt(sum);

        IO.println(sqrt);
        return sqrt;
    }
}