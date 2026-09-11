public class UsernameInspector {
    public static void main(String[] args) {

    }
    public static boolean isValidUsername(String username) {
        for (int i = 0; i < username.length(); i++) {
            if (username.charAt(i) == ' ') {
                return false;
            }
            else if (i >= '0' && i <= '9') {
                return false;
            }
        }
        char first = username.charAt(0);

        if (username.length() < 5 || username.length() > 12) {
            return false;
        }

        else if (!((first >= 'A' && first <= 'Z') || (first >= 'a' && first <= 'z'))) {
            return false;
        }

        return true;
    }

    public static int countDigits(String username) {}

    public static String initials(String firstName, String lastName)

}
