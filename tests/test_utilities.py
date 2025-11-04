import pytest

from src.utilities import remove_emojis


@pytest.mark.utility
class TestRemoveEmojis:
    """Test suite for the remove_emojis function."""

    def test_basic_emoticons(self):
        """Test removal of basic emoticon emojis."""
        text = "Hello 😀 World 😃 Test 😄"
        result = remove_emojis(text)
        assert "😀" not in result
        assert "😃" not in result
        assert "😄" not in result
        assert "Hello" in result
        assert "World" in result
        assert "Test" in result

    def test_no_emojis(self):
        """Test that text without emojis remains unchanged."""
        text = "This is a normal text without any emojis."
        result = remove_emojis(text)
        assert result == text

    def test_empty_string(self):
        """Test handling of empty string."""
        text = ""
        result = remove_emojis(text)
        assert result == ""

    def test_only_emojis(self):
        """Test text containing only emojis."""
        text = "😀😃😄😁😆"
        result = remove_emojis(text)
        assert result == ""

    def test_emojis_at_start(self):
        """Test emojis at the beginning of text."""
        text = "🎉 Congratulations on your achievement!"
        result = remove_emojis(text)
        assert "🎉" not in result
        assert result.strip() == "Congratulations on your achievement!"

    def test_emojis_at_end(self):
        """Test emojis at the end of text."""
        text = "Have a great day 😊"
        result = remove_emojis(text)
        assert "😊" not in result
        assert "Have a great day" in result

    def test_multiple_lines(self):
        """Test text with multiple lines containing emojis."""
        text = "Line 1 😀\nLine 2 😃\nLine 3 😄"
        result = remove_emojis(text)
        assert "😀" not in result
        assert "😃" not in result
        assert "😄" not in result
        assert "Line 1" in result
        assert "Line 2" in result
        assert "Line 3" in result
        assert "\n" in result  # Newlines should be preserved

    def test_special_characters_preserved(self):
        """Test that special characters (non-emoji) are preserved."""
        text = "Test @#$%^&*()_+-=[]{}|;':\",./<>?"
        result = remove_emojis(text)
        assert result == text

    def test_numbers_preserved(self):
        """Test that numbers are preserved."""
        text = "Numbers: 0123456789"
        result = remove_emojis(text)
        assert result == text

    def test_whitespace_preserved(self):
        """Test that whitespace is preserved."""
        text = "Word1    Word2\t\tWord3\n\nWord4"
        result = remove_emojis(text)
        assert result == text

    def test_unicode_text_preserved(self):
        """Test that non-emoji Unicode text is preserved."""
        text = "Café résumé naïve München"
        result = remove_emojis(text)
        assert result == text

    def test_type_error_handling(self):
        """Test that non-string input raises TypeError."""
        with pytest.raises(TypeError):
            remove_emojis(123)

        with pytest.raises(TypeError):
            remove_emojis(None)

        with pytest.raises(TypeError):
            remove_emojis(["list", "of", "strings"])

    def test_real_world_social_media_text(self):
        """Test with realistic social media text."""
        text = (
            "Just finished an amazing workout! 💪🔥 Feeling great 😊 #fitness #health"
        )
        result = remove_emojis(text)
        assert "💪" not in result
        assert "🔥" not in result
        assert "😊" not in result
        assert "Just finished an amazing workout!" in result
        assert "#fitness #health" in result

    def test_real_world_review_text(self):
        """Test with realistic product review text."""
        text = (
            "This product is amazing! ⭐⭐⭐⭐⭐ Highly recommend 👍 Will buy again 🛒"
        )
        result = remove_emojis(text)
        assert "⭐" not in result
        assert "👍" not in result
        assert "🛒" not in result
        assert "This product is amazing!" in result
        assert "Highly recommend" in result

    def test_real_world_message_text(self):
        """Test with realistic messaging text."""
        text = "Hey! 👋 Want to grab coffee later? ☕ Let me know! 😊"
        result = remove_emojis(text)
        assert "👋" not in result
        assert "☕" not in result
        assert "😊" not in result
        assert "Hey!" in result
        assert "Want to grab coffee later?" in result
        assert "Let me know!" in result

    def test_mathematical_symbols_handling(self):
        """Test handling of mathematical symbols."""
        # Some mathematical symbols might be in emoji ranges
        text = "2 + 2 = 4, π ≈ 3.14, √9 = 3"
        result = remove_emojis(text)
        # Basic math operators should be preserved
        assert "+" in result
        assert "=" in result

    def test_arrows(self):
        """Test removal of arrow symbols."""
        text = "Go right → or left ← or up ↑"
        result = remove_emojis(text)
        # Arrows might be removed as they're in emoji ranges
        assert "Go right" in result
        assert "or left" in result
        assert "or up" in result

    def test_zodiac_symbols(self):
        """Test removal of zodiac symbols."""
        text = "Aries ♈ Taurus ♉ Gemini ♊"
        result = remove_emojis(text)
        assert "♈" not in result
        assert "♉" not in result
        assert "♊" not in result
        assert "Aries" in result

    def test_weather_symbols(self):
        """Test removal of weather symbols."""
        text = "Sunny ☀️ Cloudy ☁️ Rainy ☔"
        result = remove_emojis(text)
        assert "☀" not in result
        assert "☁" not in result
        assert "☔" not in result
        assert "Sunny" in result

    def test_playing_cards(self):
        """Test removal of playing card symbols."""
        text = "Cards: ♠️ ♥️ ♦️ ♣️"
        result = remove_emojis(text)
        assert "♠" not in result
        assert "♥" not in result
        assert "♦" not in result
        assert "♣" not in result
        assert "Cards:" in result


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v"])
