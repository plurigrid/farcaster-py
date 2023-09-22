   from farcaster.bot import PsyopBot

   def test_bot():
       # Mock the Farcaster client
       farcaster = Mock()

       # Create the bot
       bot = PsyopBot(farcaster)

       # Run the bot
       bot.run()

       # Assert that the bot posted a comment for each cast
       assert farcaster.post_comment.call_count == len(farcaster.get_recent_casts())