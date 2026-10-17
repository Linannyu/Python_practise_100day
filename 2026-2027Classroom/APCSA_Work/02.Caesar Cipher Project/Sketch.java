import processing.core.PApplet;
import java.util.Scanner; // another import statement required

public class Sketch extends PApplet {
    Scanner s;
    // declare other variables here
    String origin;
    String mima = "";
    char ch;
    int shift;
    int x;
    int r,g,b;

    public void settings() {
        size(600, 600);
    } // end settings method

    public void keyPressed() {
        if (key == CODED) {
            if (keyCode == LEFT || keyCode == DOWN) {
                shift--;
            } else if (keyCode == RIGHT || keyCode == UP) {
                shift++;
            }
        }

        if (shift < 0) {
            shift = 25;
        } else if (shift > 25) {
            shift = 0;
        }
        randomColor();
        encryptMessage();
    }

    // remember, this method runs one time only!
    public void setup() {
        randomColor();
        IO.print("Enter your letter: ");
        s = new Scanner(System.in);
        origin = s.nextLine();
        IO.print("Enter your want shift: ");
        s = new Scanner(System.in);
        shift = s.nextInt();
        // origin = "Hello";
        // shift = 11;
        encryptMessage();
    } // end setup method
    
    public char encryptLetter(char ch, int shift) {
        if (Character.isLowerCase(ch)) {
            ch = (char)((ch - 'a' + shift) % 26 + 'a');
        } else if (Character.isUpperCase(ch)) {
            ch = (char)((ch - 'A' + shift) % 26 + 'A');
        }
        return ch;
    }

    public void encryptMessage() {
        mima = "";
        for (int i = 0; i < origin.length(); i++) {
            ch = origin.charAt(i);
            mima += encryptLetter(ch, shift);
        }

    }

    public void randomColor() {
        r = (int)((Math.random() * 100) + 150);
        g = (int)((Math.random() * 100) + 150);
        b = (int)((Math.random() * 100) + 150);
    }

    // rememberm this method loops 60 frames per second!
    public void draw() {
        background(r, g, b);
        // get user input on the canvas:
        fill(255,255,255);
        rect(10, 80, 580, 150, 10);
        fill(0);
        textAlign(CENTER, CENTER);
        textSize(50);
        text("Caesar Cipher", 300, 30);
        textSize(20);
        textAlign(LEFT, CENTER);
        text("Original: ", 50, 100);
        text("Encrypted: ", 50, 170);
        for (int i = 0; i < 26; i++) {
            //Show letter
            x = 20 + i * 22;
            fill(0);
            // Original
            text((char)('A' + i), x, 130);

            //Encrypted
            text(encryptLetter((char)('A' + i), shift), x, 200);
        }
        textSize(30);
        text("Original: " + origin, 50, 350);
        text("Encrypted: " + mima, 50, 400);
        text("Shift: " + shift, 50, 250);

        // text(mouseX + " " + mouseY, 30, 10);


    } // end draw method



} // end Sketch class 