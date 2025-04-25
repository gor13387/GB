import java.util.ArrayList;

public class ToyManager {
    private ArrayList<Toy> toys;

    public ToyManager() {
        toys = new ArrayList<>();
    }

    public void addToy(String id, String name, int frequency) {
        toys.add(new Toy(id, name, frequency));
    }

    public void addToysFromStrings(String[] toyStrings) {
        for (String toyString : toyStrings) {
            String[] parts = toyString.split(" ");
            String id = parts[0];
            String name = parts[1];
            int frequency = Integer.parseInt(parts[2]);
            addToy(id, name, frequency);
        }
    }

    public ArrayList<Toy> getToys() {
        return toys;
    }
}
