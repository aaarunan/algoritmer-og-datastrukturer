import java.nio.charset.CharacterCodingException;
import java.util.LinkedList;
import java.util.Random;
import java.util.Scanner;

class Node<T> {
    private T value;
    private Node right;
    private Node left;

    public Node(T value) {
        this.value = value;
    }

    public Node() {
    }

    public T getValue() {
        return value;
    }

    public void setValue(T value) {
        this.value = value;
    }

    public Node<T> getLeft() {
        return left;
    }

    public Node<T> getRight() {
        return right;
    }

    public Node<T> getLast() {
        if (this.getRight() == null) {
            return this;
        } else {
            return this.getRight().getLast();
        }
    }

    public Node<T> getFirst() {
        if (this.getLeft() == null) {
            return this;
        } else {
            return this.getLeft().getFirst();
        }
    }

    public void insertLast(T value) {
        if (this.value == null) {
            this.value = value;
        } else {
            Node last = this.getLast();
            Node newNode = new Node(value);
            newNode.setLeft(last);
            last.setRight(newNode);
        }
    }

    public void insertFirst(T value) {
        if (this.value == null) {
            this.value = value;
        } else {
            Node first = this.getFirst();
            Node newNode = new Node(value);
            first.setLeft(newNode);
            newNode.setRight(first);
        }
    }

    public void setRight(Node right) {
        this.right = right;
    }

    public void setLeft(Node left) {
        this.left = left;
    }

    @Override
    public String toString() {
        Node last = this.getFirst();
        StringBuilder result = new StringBuilder();
        while (last != null) {
            result.append(last.getValue());
            last = last.getRight();

        }
        return result.toString();
    }
}

public class Oppgave4 {

    public static void main(String[] args) {
        System.out.println(testAddition(100000));
        System.out.println(testSubtraction(100000));

        Scanner sc = new Scanner(System.in);
        boolean loop = true;

        while (loop) {
            System.out.println("Type nums1:");
            Node<Character> nums1 = parseInput(sc.nextLine());
            System.out.println("Type nums2:");
            Node<Character> nums2 = parseInput(sc.nextLine());

            System.out.println("Choose operation:");
            System.out.println("1. Addtion");
            System.out.println("2. Subtraction");
            System.out.println("3. Exit");

            switch (sc.nextInt()) {
                case 1:
                    System.out.println(removeTrailingZeroes(addition(nums1, nums2)));
                    break;
                case 2:
                    System.out.println(removeTrailingZeroes(subtract(nums1, nums2)));
                    break;
                case 3:
                    loop = false;
                    sc.close();
                    System.exit(0);
                    break;
            }
            sc.nextLine();
        }
    }

    private static Node<Character> addition(Node<Character> nums1, Node<Character> nums2) {
        Node<Character> result = new Node();
        Node<Character> last1 = nums1.getLast();
        Node<Character> last2 = nums2.getLast();

        int sum = 0;
        int temp = 0;
        int num1 = 0;
        int num2 = 0;

        while (last1 != null || last2 != null) {

            if (last1 != null) {
                num1 = Character.getNumericValue(last1.getValue());
                last1 = last1.getLeft();
            } else {
                num1 = 0;
            }
            if (last2 != null) {
                num2 = Character.getNumericValue(last2.getValue());
                last2 = last2.getLeft();
            } else {
                num2 = 0;
            }
            sum = num1 + num2 + temp;
            result.insertFirst((char) (sum % 10 + '0'));
            temp = sum / 10;
        }
        if (temp != 0) {
            result.insertFirst((char) (temp + '0'));
        }

        return result;
    }

    private static Node<Character> subtract(Node<Character> nums1, Node<Character> nums2) {
        Node<Character> result = new Node();

        int diff = 0;
        int num1 = 0;
        int num2 = 0;
        Node<Character> last1 = nums1.getLast();
        Node<Character> last2 = nums2.getLast();

        while (last1 != null || last2 != null) {
            if (last1 != null) {
                num1 = Character.getNumericValue(last1.getValue());
                last1 = last1.getLeft();
            } else {
                num1 = 0;
            }
            if (last2 != null) {
                num2 = Character.getNumericValue(last2.getValue());
                last2 = last2.getLeft();
            } else {
                num2 = 0;
            }
            diff = num1 - num2;
            if (diff < 0) {
                if (nums1 == null) {
                    throw new IllegalStateException("Result is negative");
                }
                last1.setValue((char) (Character.getNumericValue(last1.getValue()) - 1 + '0'));
                diff += 10;
            }
            result.insertFirst((char) (diff + '0'));
        }
        return result;
    }

    private static Node<Character> removeTrailingZeroes(Node<Character> node) {
        Node<Character> first = node.getFirst();
        while (first != null) {
            int value = Character.getNumericValue(first.getValue());
            if (value > 0) {
                break;
            }
            if (first.getRight() == null) {
                break;
            }
            first = first.getRight();
            if (value == 0) {
                first.setLeft(null);
            }
        }
        return first;
    }

    private static Node<Character> parseInput(String string) {
        Node<Character> nums = new Node();
        for (char num : string.toCharArray()) {
            if (!Character.isDigit(num)) {
                throw new IllegalArgumentException("Not a number");
            }
            nums.insertLast(num);
        }
        return nums;
    }

    private static boolean testAddition(int n) {
        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            int num1 = Math.abs(rand.nextInt())/10;
            int num2 = Math.abs(rand.nextInt())/10;
            int sum = num1 + num2;
            int sum2 = Integer.parseInt(addition(parseInput(Integer.toString(num1)), parseInput(Integer.toString(num2))).toString());
            if (sum != sum2) {
                return false;
            }
        }
        return true;
    }

    private static boolean testSubtraction(int n) {
        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            int num1 = Math.abs(rand.nextInt())/10;
            int num2 = Math.abs(rand.nextInt())/10;
            if (num1-num2 < 0) {
                int temp = num1;
                num1 = num2;
                num2 = temp;
            }
            int sum = num1 - num2;
            int sum2 = Integer.parseInt(subtract(parseInput(Integer.toString(num1)), parseInput(Integer.toString(num2))).toString());
            if (sum != sum2) {
                return false;
            }
        }
        return true;
    }
}