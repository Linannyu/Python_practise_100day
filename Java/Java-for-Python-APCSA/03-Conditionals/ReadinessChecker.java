public class ReadinessChecker {
    public static void main(String[] args) {
        int completedLabs = 2;
        int averageScore = 80;
        boolean hasReviewedMistakes = true;
        String goal = "AP CSA";

        // TODO: write one ordered if / else if / else chain
        if (averageScore < 0 || averageScore > 100) {
            System.out.println("Invalid average score.");
        } else if (averageScore < 60) {
            System.out.println("Review basics before moving on.");
        } else if (!hasReviewedMistakes) {
            System.out.println("Review your mistakes, then retry.");
        } else if (completedLabs >= 3 && goal.equals("AP CSA")) {
            System.out.println("Ready for AP CSA practice.");
        } else {
            System.out.println("Keep building your foundation.");
        }

    }
}