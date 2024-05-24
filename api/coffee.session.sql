-- Create Flavors table
CREATE TABLE Flavors (
    FlavorID INTEGER PRIMARY KEY AUTOINCREMENT,
    Description TEXT NOT NULL
);

-- Create Milks table
CREATE TABLE Milks (
    MilkID INTEGER PRIMARY KEY AUTOINCREMENT,
    Description TEXT NOT NULL
);

-- Create Sizes table
CREATE TABLE Sizes (
    SizeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Description TEXT NOT NULL
);

-- Create Orders table
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    ChosenMilkID INTEGER,
    ChosenSizeID INTEGER,
    FOREIGN KEY (ChosenMilkID) REFERENCES Milks(MilkID),
    FOREIGN KEY (ChosenSizeID) REFERENCES Sizes(SizeID)
);

-- Create OrderFlavors table to track the many-to-many relationship between Orders and Flavors
CREATE TABLE OrderFlavors (
    OrderFlavorID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderID INTEGER,
    FlavorID INTEGER,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (FlavorID) REFERENCES Flavors(FlavorID)
);







-- Insert rows into Sizes table
INSERT INTO Sizes (Description) VALUES ('Small');
INSERT INTO Sizes (Description) VALUES ('Medium');
INSERT INTO Sizes (Description) VALUES ('Large');
INSERT INTO Sizes (Description) VALUES ('Extra Large');






-- Insert rows into Milks table
INSERT INTO Milks (Description) VALUES ('Whole Milk');
INSERT INTO Milks (Description) VALUES ('Skim Milk');
INSERT INTO Milks (Description) VALUES ('Soy Milk');
INSERT INTO Milks (Description) VALUES ('Almond Milk');
INSERT INTO Milks (Description) VALUES ('Oat Milk');
INSERT INTO Milks (Description) VALUES ('Coconut Milk');
INSERT INTO Milks (Description) VALUES ('Lactose-Free Milk');
INSERT INTO Milks (Description) VALUES ('Half-and-Half');






-- Insert rows into Flavors table
INSERT INTO Flavors (Description) VALUES ('Vanilla');
INSERT INTO Flavors (Description) VALUES ('Caramel');
INSERT INTO Flavors (Description) VALUES ('Hazelnut');
INSERT INTO Flavors (Description) VALUES ('Mocha');
INSERT INTO Flavors (Description) VALUES ('Pumpkin Spice');
INSERT INTO Flavors (Description) VALUES ('Peppermint');
INSERT INTO Flavors (Description) VALUES ('Cinnamon');
INSERT INTO Flavors (Description) VALUES ('Toffee Nut');
INSERT INTO Flavors (Description) VALUES ('Irish Cream');
INSERT INTO Flavors (Description) VALUES ('Coconut');
INSERT INTO Flavors (Description) VALUES ('White Chocolate');
INSERT INTO Flavors (Description) VALUES ('Raspberry');




-- Add price column to Milks table
ALTER TABLE Milks
ADD COLUMN Price REAL;

-- Add price column to Sizes table
ALTER TABLE Sizes
ADD COLUMN Price REAL;

-- Add price column to Flavors table
ALTER TABLE Flavors
ADD COLUMN Price REAL;

-- Update Milks table with random prices
UPDATE Milks
SET Price = ROUND(ABS(RANDOM() % 226) / 100.0 + 0.25, 2);

-- Update Sizes table with random prices
UPDATE Sizes
SET Price = ROUND(ABS(RANDOM() % 226) / 100.0 + 0.25, 2);

-- Update Flavors table with random prices
UPDATE Flavors
SET Price = ROUND(ABS(RANDOM() % 226) / 100.0 + 0.25, 2);


SELECT
    o.OrderID,
    o.ChosenMilkID,
    o.ChosenSizeID,
    m.Description AS MilkDescription,
    m.MilkID,
    s.Description AS SizeDescription,
    s.SizeID,
    s.Price AS SizePrice,
    m.Price AS MilkPrice,
    GROUP_CONCAT(f.FlavorID || '|' || f.Description || '|' || f.Price, ',') AS Flavors
FROM Orders o
JOIN Milks m ON m.MilkID = o.ChosenMilkID
JOIN Sizes s ON s.SizeID = o.ChosenSizeID
JOIN OrderFlavors of ON of.OrderID = o.OrderID
JOIN Flavors f ON f.FlavorID = of.FlavorID
GROUP BY o.OrderID, o.ChosenMilkID, o.ChosenSizeID, m.Description, m.MilkID, s.Description, s.SizeID, s.Price, m.Price;
