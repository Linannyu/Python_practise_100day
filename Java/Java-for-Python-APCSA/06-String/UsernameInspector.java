public class UsernameInspector {
    public static void main(String[] args) {
        String username = "1lin2026";
        System.out.println("Username: " + username);
        System.out.println("Is valid: " + isValidUsername(username));
        System.out.println("Digits: " + countDigits(username));

        String firstName = "Lin";
        String lastName = "Zhang";
        System.out.println("Initials: " + initials(firstName, lastName));
    }

    public static boolean isValidUsername(String username) {
        for (int i = 0; i < username.length(); i++) {
            if (username.charAt(i) == ' ') {
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
        
        boolean hasDigit = false;
        for (int a = 0; a < username.length(); a++) {
            char character = username.charAt(a);
            if (character >= '0' && character <= '9') {
                hasDigit = true;
            }
        }

        if (!hasDigit) {
            return false;
        }


        return true;
    }

    /* 统计字符串中数字的个数 */
    public static int countDigits(String username) {
        int count = 0;  // 用于计数的变量，初始化为0
        // 遍历字符串中的每一个字符
        for (int i = 0; i < username.length(); i++) {
            char c = username.charAt(i);  // 获取当前字符
            // 检查当前字符是否为数字字符（0-9）
            if (c >= '0' && c <= '9') {
                count++;  // 如果是数字字符，计数器加1
            }
        }
        // 返回统计结果
        return count;
    }

    public static String initials(String firstName, String lastName) {
        // 获取名字的首字母并转换为大写
        char firstInitial = Character.toUpperCase(firstName.charAt(0));
        // 获取姓氏的首字母并转换为大写
        char lastInitial = Character.toUpperCase(lastName.charAt(0));
        // 将两个首字母组合成一个字符串并返回
        return firstInitial + "." + lastInitial + ".";
    }

    public static String maskUsername(String username) {
        char firstChar = username.charAt(0);
        char lastChar = username.charAt(username.length() - 1);
        int middleLength = username.length() - 2;
        return firstChar + "*".repeat(middleLength) + lastChar;
    }
}
    
