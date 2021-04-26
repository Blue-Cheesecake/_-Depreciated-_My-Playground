// https://leetcode.com/problems/long-pressed-name/

public class Test_LongPressedName {

    public boolean isLongPressedName(String name, String typed) {

        if (name.length() == 0 && typed.length() == 0) {
            return true;
        }
        if (name.length() == 0 && typed.length() != 0) {
            return false;
        }

        Character lastChar = name.charAt(0);
        boolean checkNext = false;
        // boolean clean = false;

        int j = 0;
        int i = 0;
        for (i = 0; i < name.length(); i++) {

            Character chaName = name.charAt(i);
            if (j >= typed.length()) {
                return false;
            }
            Character chaType = typed.charAt(j);

            if (checkNext) {
                if (chaName == chaType) {
                    lastChar = chaName;
                    j++;
                    // i--;
                } else {
                    if (lastChar != chaType) {
                        return false;
                    }
                    // clean state
                    while (lastChar == chaType) {
                        j++;
                        if (j >= typed.length()) {
                            j--;
                            break;
                        }
                        chaType = typed.charAt(j);
                    }
                    checkNext = false;
                    i--;

                }
                // i--;
                continue;
            }

            if (chaName == chaType) {
                lastChar = chaName;
                checkNext = true;
                j++;
                // i--;
            } else {
                return false;
            }

        }

        for (int k = j; k < typed.length(); k++) {
            if (typed.charAt(k) != lastChar) {
                return false;
            }
        }

        return true;

    }

}
