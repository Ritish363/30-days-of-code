import java.util.*;

public class Day_7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();

        int number = rand.nextInt(100) + 1;
        int attempts = 7;

        System.out.println("Guess the number (1-100)");
        System.out.println("You have 7 attempts");

        while (attempts > 0) {
            System.out.print("Enter guess: ");
            int guess = sc.nextInt();

            int diff = Math.abs(number - guess);

            if (guess == number) {
                System.out.println("Correct! You win");
                return;
            } else if (diff <= 5) {
                System.out.println("Very close!");
            } else if (diff <= 15) {
                System.out.println("Close!");
            } else {
                System.out.println("Far!");
            }

            attempts--;
            System.out.println("Attempts left: " + attempts);
        }

        System.out.println("Game Over! Number was: " + number);
    }
}