-- Message Table
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
-- Likes Table
CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    message_id INTEGER REFERENCES messages(id),
    created_at TIMESTAMP DEFAULT NOW()
);


-- trigger
CREATE OR REPLACE FUNCTION update_message_likes() RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        UPDATE messages SET likes = likes + 1 WHERE id = NEW.message_id;
    ELSIF TG_OP = 'DELETE' THEN
        UPDATE messages SET likes = likes - 1 WHERE id = OLD.message_id;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_likes_count
AFTER INSERT OR DELETE ON likes
FOR EACH ROW
EXECUTE FUNCTION update_message_likes();
