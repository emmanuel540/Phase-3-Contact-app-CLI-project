
import click
from sqlalchemy.orm import Session
from models import Base, engine, Category, Contact

Base.metadata.create_all(bind=engine)
session = Session(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
def add_contact():
    """Add a new contact."""
    click.echo("Adding a new contact...")

    name = click.prompt("Enter the contact name")
    phone_number = click.prompt("Enter the phone number")
    email = click.prompt("Enter the email address")
    notes = click.prompt("Enter any additional notes")

    
    existing_categories = session.query(Category).all()
    click.echo("Existing categories:")
    for category in existing_categories:
        click.echo(f"{category.id}: {category.name}")

    category_id = click.prompt("Enter the category ID for the contact")

    
    category = session.query(Category).get(category_id)
    if category is None:
        click.echo("Error: Category not found.")
        return

    
    new_contact = Contact(
        name=name,
        phone_number=phone_number,
        email=email,
        notes=notes,
        category=category,
    )

    
    session.add(new_contact)
    session.commit()

    click.echo("Contact added successfully.")

@cli.command()
def view_contacts():
    """View contacts."""
    click.echo("Viewing contacts...")

