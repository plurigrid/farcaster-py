   from farcaster import Farcaster

   class PsyopBot:
       def __init__(self, farcaster):
           self.farcaster = farcaster

       def run(self):
           # Get recent casts
           casts = self.farcaster.get_recent_casts()

           # For each cast, post a comment promoting the duck cause
           for cast in casts:
               self.farcaster.post_comment(cast.id, "Support the #DuckCause!")

   if __name__ == "__main__":
       farcaster = Farcaster("<MNEMONIC_ENV_VAR>")
       bot = PsyopBot(farcaster)
       bot.run()