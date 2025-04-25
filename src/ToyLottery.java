import java.util.Random;
import java.util.ArrayList;
public class ToyLottery {
    private ArrayList<Toy> toyList;

    public ToyLottery(ArrayList<Toy> toys) {
        this.toyList = toys;
    }
    
    public String getToy() {
        Random random = new Random();
        int randomValue = random.nextInt(100);

        if (randomValue < 20) {
            return "1 конструктор"; // 20% шанс на 1
        } else if ((randomValue < 40)&(randomValue > 20)){
            return "2 робот"; // 20% шанс на 2
        } else {
            return "3 кукла"; // 60% шанс на 3
        }
    }
}

