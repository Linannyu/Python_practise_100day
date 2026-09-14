import java.util.Arrays;

public class ScoreAnalyzer {
    public static void main(String[] args) {
        int[] scores = {88, 72, 72, 95};

        System.out.println("Highest: " + highestScore(scores));
        System.out.println("Passing: " + countPassing(scores));
        System.out.println("First at least 90: " + firstScoreAtLeast(scores, 90));
        addCurve(scores, 5);
        System.out.println(Arrays.toString(scores));
        System.out.println("Has consecutive duplicates: " + hasConsecutiveDuplicates(scores));
    }
    public static int highestScore(int[] scores) {
        int max = scores[0];
        for (int score : scores) {
            if (score > max) {
                max = score;
            }
        }
        return max;
    }

    public static int countPassing(int[] scores) {
        int count = 0;
        for (int score : scores) {
            if (score >= 60) {
                count++;
            }
        }
        return count;
    }
    public static int firstScoreAtLeast(int[] scores, int target) {
        for (int i = 0;i < scores.length; i++) {
            if (scores[i] >= target) {
                return i;
            }
        }
        return -1; 
    }
    public static void addCurve(int[] scores, int points) {
        for (int i = 0; i < scores.length; i++) {
            scores[i] += points;
            if (scores[i] > 100) {
                scores[i] = 100;
            }
        }
    }

    public static boolean hasConsecutiveDuplicates(int[] scores) {
        for (int i = 0; i < scores.length - 1; i++) {
            if (scores[i] == scores[i + 1]) {
                return true;
            }
        }
        return false;
    }


}
