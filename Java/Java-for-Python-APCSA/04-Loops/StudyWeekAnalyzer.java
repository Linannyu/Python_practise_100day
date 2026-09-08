public class StudyWeekAnalyzer {
    public static void main(String[] args) {
        int[] minutes = {35, 0, 50, 80, 20, 65, 40};
        //int[] minutes = {0, 0, 0, 0, 0, 0, 0};
        //int[] minutes = {60, 0, 0, 0, 0, 0, 0};


        int total_minutes = 0;
        int total_days = 0;
        int active_days = 0;
        int strong_day = 0;
        double average_minutes = 0;
        int first_strong_day_index = -1;
        for (int i = 0; i < minutes.length; i++) {
            total_minutes += minutes[i];
            total_days++;
            if (minutes[i] > 0) {
                active_days++;
            }

            if (minutes[i] >= 60) {
                strong_day++;
            }
        }
        for (int i = 0; i < minutes.length; i++) {
            if (minutes[i] >= 60) {
                first_strong_day_index = i;
                break;
            }
        }
        average_minutes = (double) total_minutes / (double) total_days;

        System.out.println("Total minutes: " + total_minutes);
        System.out.println("Active days: " + active_days);
        System.out.println("Strongest day: " + strong_day);
        System.out.println("Average minutes: " + average_minutes);
        System.out.println("First strong day index: " + first_strong_day_index);
        
        for (int i = 0; i < minutes.length; i++) {
            if (minutes[i] == 0) {
                continue;
            }
        
        System.out.println("Day " + i + ": " + minutes[i]);
        }

    }
}