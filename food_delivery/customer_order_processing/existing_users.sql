INSERT INTO auth_user (id, username, password, first_name, last_name, email, is_staff, is_active, date_joined)
VALUES 
    (1, 'john_doe', 'pbkdf2_sha256$600000$f5N8Rv6hdD6P$89de9c2e0ef31e4302a4b2b9fba2436d7b9b5a7db0930b4d2bb6f332c833dcd8', 'John', 'Doe', 'john@example.com', 0, 1, NOW()),
    (2, 'alice_smith', 'pbkdf2_sha256$600000$gH2sM56JpXvE$c58eaad67e5b37aa4c33e0f02e9d7acb7db4c8d639b2e4f6b7d2df4e5e8a7fbb', 'Alice', 'Smith', 'alice@example.com', 0, 1, NOW());

INSERT INTO customer_order_processing_customer (user_ptr_id, address, contact, payment_details, special_instructions)
VALUES 
    (1, '123 Main St', '9876543210', 'VISA ****1234', 'Allergic to peanuts'),
    (2, '456 Park Ave', '8765432109', 'MasterCard ****5678', 'No spicy food');
