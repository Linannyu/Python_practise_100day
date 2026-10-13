import processing.core.PApplet;
import java.util.Scanner;

public class Sketch extends PApplet {
    Scanner s,d;
    String name,last_name,first_name;
    String pronouns;
    int tagColor;
    int space = -1;
    public void settings() {
        size(600, 600);
    } // TO DO: comment this closing bracket!

    public void setup() {
        s = new Scanner(System.in);
        // get user input (two times)
        while (space == -1) {
            IO.print("Please enter your fullname:");
            name = s.nextLine();
            space = name.indexOf(" ");
        }
        // do work with the user input (String methods)
        
        last_name = name.substring(space + 1);
        first_name = name.substring(0, space);

        if (first_name.toLowerCase().compareTo(last_name.toLowerCase()) < 0) {
            first_name = first_name.toUpperCase();
            last_name = last_name.toUpperCase();
        }
        if (last_name.length() > first_name.length()) {
            last_name = last_name.substring(0,1);
        }
        name = first_name + ' ' + last_name;


        IO.print("What is your pronoun?:");
        pronouns = s.next().toLowerCase();

        if (pronouns.equals("he") || pronouns.equals("him")) {
            tagColor = color(102, 255, 236);
        } else if (pronouns.equals("she") || pronouns.equals("her")) {
            tagColor = color(255, 102, 255);
        } else if (pronouns.equals("they") || pronouns.equals("them")) {
            tagColor = color(145, 0, 255);
        } else {
            tagColor = color(0);
        }

    } // TO DO: comment this closing bracket!

    public void draw() {
        background(220);
        noStroke();
        fill(255, 255, 255);
        rect(95, 195, 410, 260, 10);
        // design your name tag here:
        fill(tagColor);
        rect(100, 200, 400, 250, 10);

        fill(255, 255, 255);
        rect(110, 320, 380, 120, 10);
        
        fill(0);
        textAlign(CENTER,CENTER);
        textSize(10);
        text(mouseX + " " + mouseY, 100, 100);
        textSize(70);
        fill(255, 255, 255);
        text("Hello", 300, 230);
        textSize(50);
        text("MY NAME IS", 300, 290);

        textSize(50);
        fill(0);
        text(name, 300, 370);



        
    } // TO DO: comment this closing bracket!

    // other methods go here:



} // end Sketch class