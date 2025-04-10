import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Collections;

class Student implements Comparable<Student> {
	private String name;
	private int kor;
	private int eng;
	private int math;

	public Student(String name, int kor, int eng, int math) {
		this.name = name;
		this.kor = kor;
		this.eng = eng;
		this.math = math;
	}

	public String getName() {
		return name;
	}

	@Override
	public int compareTo(Student o) {
		if (this.kor == o.kor && this.eng == o.eng && this.math == o.math) {
			return this.name.compareTo(o.name);
		}
		if (this.kor == o.kor && this.eng == o.eng) {
			return Integer.compare(o.math, this.math);
		}
		if (this.kor == o.kor) {
			return Integer.compare(this.eng, o.eng);
		}

		return Integer.compare(o.kor, this.kor);
	}
}

class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		List<Student> students = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			String name = sc.next();
			int kor = sc.nextInt();
			int eng = sc.nextInt();
			int m = sc.nextInt();
			students.add(new Student(name, kor, eng, m));
		}

		Collections.sort(students);

		for (int i = 0; i < n; i++) {
			System.out.println(students.get(i).getName());
		}
	}
}
