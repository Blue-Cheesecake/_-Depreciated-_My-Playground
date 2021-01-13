package Basic;

public class Test_GoldParser {

    public String interpret(String command) {

        if (command.length() == 0) {
            return "";
        }

        if (command.charAt(0) == 'G') {
            return "G" + interpret(command.substring(1));
        }

        if (command.length() >= 2) {
            if (command.substring(0, 2).equals("()")) {
                return "o" + interpret(command.substring(2));
            }
        }

        if (command.length() >= 4) {
            if (command.substring(0, 4).equals("(al)")) {
                return "al" + interpret(command.substring(4));
            }
        }

        return interpret(command.substring(1));
    }
}
