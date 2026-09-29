import processing.core.PApplet;
import java.util.Scanner; // another import statement required

public class Sketch extends PApplet {
    Scanner s;
    // declare other variables here
    String origin;
    String mima = "";

    public void settings() {
        size(600, 600);
    } // end settings method

    // remember, this method runs one time only!
    public void setup() {
        s = new Scanner(System.in);
        origin = s.nextLine();
        for (int i = 0; i < origin.length(); i++) {
            char ch =  origin.charAt(i);
            if (Character.isLetter(ch)) {
                // ch = (char)(ch + 3);
                if (Character.isLowerCase(ch)) {
                    ch = (char)((ch - 'a' + 11) % 26 + 'a');
                } else {
                    ch = (char)((ch - 'A' + 11) % 26 + 'A');
                }
                mima += ch;

            } else if (Character.isDigit(ch)){
                IO.println("This is isDigit");
            } else {
                IO.println("no thing");
            }

        }
        IO.println(mima);


        
    } // end setup method

    // rememberm this method loops 60 frames per second!
    public void draw() {
        background(220);

        // get user input on the canvas:
        fill(0);
        textSize(48);
        text("toCaesar", 100, 100);
        text(origin, width/2, height/2);
        text(mima, width/2, height/3);
    } // end draw method

} // end Sketch class