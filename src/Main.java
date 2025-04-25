import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        ToyManager toyManager = new ToyManager();

        // Входные данные
        String[] toyStrings = {
            "1 конструктор 2",
            "2 робот 2",
            "3 кукла 6"
        };

        toyManager.addToysFromStrings(toyStrings);

        ToyLottery lottery = new ToyLottery(toyManager.getToys());

        try (BufferedWriter writer = new BufferedWriter(new FileWriter("lottery_results.txt"))) {
            for (int i = 0; i < 10; i++) {
                String drawnToyId = lottery.getToy();
                writer.write("Выпала игрушка с ID: " + drawnToyId + "\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

