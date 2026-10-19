import processing.core.PApplet;

public class Sketch extends PApplet {
    int molesize;
    int width,height;
    int r,g,b;

    /**
     * settings()函数在processing中用于设置程序的基本参数
     * 这个函数在setup()函数之前执行，且只执行一次
     * 通常用于设置画布大小、渲染器等
     */
    public void settings() {
        size(600, 600); // 设置画布大小为600x600像素
    }

    public void setup() {
        spawnTarget();
    }

    public void draw() {
        background(7, 166, 240);
        fill(r, g, b);
        circle(width, height, molesize);
        // if (frameCount % 30 == 0) {
        //     width = (int)((Math.random() * 501) + 100);
        //     height = (int)((Math.random() * 501) + 100);
        // }

    }

    public void mousePressed() {
        if ((int)(Math.random() * 10) > 2) {
            IO.println("click");
        } else {
            IO.println("ouch!");
        }
        spawnTarget();
    }

    public void spawnTarget() {
        molesize = (int)((Math.random() * 51) + 50);
        r = (int)(Math.random() * 255);
        g = (int)(Math.random() * 255);
        b = (int)(Math.random() * 255);

    }
}