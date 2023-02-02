package finaltest;

public class BookBean {
	private String title;
	private String author;
	private String publisher;
	
	public BookBean(String title, String author, String publisher) {
		super();
		this.title = title;
		this.author = author;
		this.publisher = publisher;
	}
	
	public String getTitle() {
		return title;
	}
	
	public String getAuthor() {
		return author;
	}
	
	public String getPublisher() {
		return publisher;
	}

	public void setTitle() {
		this.title = title;
	}
	
	public void setAuthor() {
		this.author = author;
	}
	
	public void setPublisher() {
		this.publisher = publisher;
	}
	
	public String toString() {
		return title + "/" + author + "/" + publisher;
	}
	
}
