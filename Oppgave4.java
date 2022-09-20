import java.nio.charset.CharacterCodingException;
import java.util.LinkedList;
import java.util.Scanner;

class Node<T> {
    public T value;
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

    public void print() {
        Node last = this.getFirst();
        while (last != null) {
            System.out.print(last.getValue());
            last = last.getRight();
        }
        System.out.println();
    }

}

public class Oppgave4 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {

            System.out.println("Type nums1:");
            Node<Character> nums1 = parseInput(sc.nextLine());
            System.out.println("Type nums2:");
            Node<Character> nums2 = parseInput(sc.nextLine());

            System.out.println("Choose operation:");
            System.out.println("1. Addtion");
            System.out.println("2. Subtraction");

            switch (sc.nextInt()) {
                case 1:
                    addition(nums1, nums2).print();
                    break;
                case 2:
                    subtract(nums1, nums2).print();
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
                num2 = 0;
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
        boolean loaner = false;

        while (last1 != null || last2 != null) {
            if (last1 != null) {
                num1 = Character.getNumericValue(last1.getValue());
                last1 = last1.getLeft();
            } else {
                num2 = 0;
            }
            if (last2 != null) {
                num2 = Character.getNumericValue(last2.getValue());
                last2 = last2.getLeft();
            } else {
                num2 = 0;
            }
            if (loaner) {
                num1 -= 1;
                loaner = false;
            }
            diff = num1 - num2;
            if (diff < 0) {
                if (nums1.getLeft() == null) {
                    throw new IllegalArgumentException("Result is negative");
                }
                loaner = true;
                diff += 10;
            }
            result.insertFirst((char) (diff + '0'));
        }
        return result;
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
}