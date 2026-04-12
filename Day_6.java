import java.util.*;

class Question {
    String question;
    String[] options;
    int correctAnswer;

    Question(String question, String[] options, int correctAnswer) {
        this.question = question;
        this.options = options;
        this.correctAnswer = correctAnswer;
    }

    void display() {
        System.out.println(question);
        for (int i = 0; i < options.length; i++) {
            System.out.println((i + 1) + ". " + options[i]);
        }
    }
}

public class Day_6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ArrayList<Question> quiz = new ArrayList<>();

        quiz.add(new Question(
            "What is the capital of India?",
            new String[]{"Mumbai", "New Delhi", "Chennai", "Kolkata"},
            2
        ));

        quiz.add(new Question(
            "In which year did India conduct its first nuclear test at Pokhran??",
            new String[]{"1974", "1998", "1962", "1985"},
            1
        ));

        quiz.add(new Question(
            "Who is India's Foreign external minister",
            new String[]{"Rajnath Singh", "Nirmala Sitharaman", "S. Jaishankar", "Amit Shah"},
            3
        ));

        int score = 0;

        for (Question q : quiz) {
            q.display();
            System.out.print("Enter your answer number: ");
            int ans = sc.nextInt();

            if (ans == q.correctAnswer) {
                System.out.println("Correct!\n");
                score++;
            } else {
                System.out.println("Wrong!\n");
            }
        }

        System.out.println("Your final score: " + score + "/" + quiz.size());
    }
}