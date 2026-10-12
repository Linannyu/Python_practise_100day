import processing.core.PApplet;
import java.util.Scanner;

public class Sketch extends PApplet {
    Scanner s,d;
    String name,last_name,first_name;
    String pronouns;
    String tagColor;
    int space = -1;
    public void settings() {
        size(600, 600);
    } // TO DO: comment this closing bracket!

    public void setup() {
        s = new Scanner(System.in);
        d = new Scanner(System.in);
        // get user input (two times)
        while (space == -1) {
            IO.print("Please enter your fullname:");
            name = s.nextLine();
            space = name.indexOf(" ");
        }
        // do work with the user input (String methods)
        
        last_name = name.substring(space + 1);
        first_name = name.substring(0, space);

        IO.println(last_name.compareTo(first_name) );

        IO.print("What is your pronoun?:");
        pronouns = d.next();

        if (pronouns.equals("he") || pronouns.equals("him")) {
            tagColor = "blue";
        } else if (pronouns.equals("she") || pronouns.equals("her")) {
            tagColor = "pink";
        } else if (pronouns.equals("they") || pronouns.equals("them")) {
            tagColor = "purple";
        }
        



    } // TO DO: comment this closing bracket!

    public void draw() {
        background(220);
        // design your name tag here:
        if (tagColor.equals("blue")) {
            fill(102, 255, 236);
        } else if (tagColor.equals("pink")) {
            fill(255, 255, 255);
        } else if (tagColor.equals("purple")) {
            fill(255, 255, 255);
        }
        rect(100, 200, 400, 250, 10);

        fill(255, 255, 255);
        rect(110, 320, 380, 120, 10);
        fill(0);
        textSize(10);
        text(mouseX + " " + mouseY, 100, 100);
        textSize(70);
        text("Hello", 230, 260);
        textSize(50);
        text("MY NAME IS", 180, 305);

        textSize(50);
        text(name, 180, 380);



        
    } // TO DO: comment this closing bracket!

    // other methods go here:



} // end Sketch class