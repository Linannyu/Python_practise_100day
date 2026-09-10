public class StudyToolkit {
    public static void main(String[] args) {
        int[] minutes = {35, 0, 50, 80, 20, 65, 40};
        int minimum = 60;
        int goal = 420;
        System.out.println("Total minutes: " + totalMinutes(minutes));
        System.out.println("countStrongDays: " + countStrongDays(minutes, minimum));
        System.out.println("Average minutes: " + averageMinutes(minutes));
        System.out.println("First day at least " + minimum + ": " + firstDayAtLeast(minutes, minimum));
        System.out.println("Met weekly goal: " + metWeeklyGoal(minutes, goal));
    }
    public static int totalMinutes(int[] values) {
        int total = 0;
        for (int i = 0; i < values.length; i++) {
            total += values[i];
        }
        return total;
    }
    public static int countStrongDays(int[] values, int minimum) {
        int count = 0;
        for (int i = 0; i < values.length; i++) {
            if (values[i] >= minimum) {
                count++;
            }
        }
        return count;
    }
    public static double averageMinutes(int[] values) {
        int total = totalMinutes(values);
        return (double) total / values.length;
    }
    public static int firstDayAtLeast(int[] values, int minimum) {
        for (int i = 0; i < values.length; i++) {
            if (values[i] >= minimum) {
                return i;
            }
        }
        return -1;
    }
    public static boolean metWeeklyGoal(int[] values, int goal) {
        int total = totalMinutes(values);
        return total >= goal;
    }
}
