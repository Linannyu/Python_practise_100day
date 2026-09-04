public class StudyReceipt {
    public static void main(String[] args) {
        String learner = "Lin";
        int minutes = 125;
        int completed = 2;
        int target = 3;
        double snackCost = 2.50;

        // TODO：计算并打印报告
        int hours = minutes / 60;
        int min = minutes % 60;
        double average = completed * 1.0 / target;
        boolean isGoalReached = completed >= target;
        System.out.println(hours + " hours " + min + " minutes");
        System.out.println("Average: " + average);
        System.out.println("Goal reached: " + isGoalReached);

        //Stretch goal
        double curseFee = 10.00;
        double totalCost = snackCost + curseFee;
        System.out.println("Total snack cost: $" + totalCost);
    }
}
