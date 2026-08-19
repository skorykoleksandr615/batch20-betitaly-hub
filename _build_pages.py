from pathlib import Path

OFFER = "https://dscdscds913.online/ctrhdZXV?sub_id_1=betitaly"
ROOT = Path(r"C:\AndroidStudioProjects\batch20-hubs\betitaly")
LANGS = "en de ru uk pl es pt fr it tr nl".split()

NAV = [
    ("/", "Home"),
    ("/bi-login.html", "Login"),
    ("/bi-join.html", "Register"),
    ("/bi-bonus.html", "Bonus"),
    ("/bi-slots.html", "Slots"),
    ("/bi-odds.html", "Odds"),
    ("/bi-crash.html", "Crash"),
    ("/bi-live.html", "Live"),
    ("/bi-app.html", "App"),
    ("/bi-pay.html", "Pay"),
    ("/bi-help.html", "Help"),
]

PAGES = [
    dict(
        slug="bi-login.html",
        nav="Login",
        title="BetItaly Login Guide | betitaly.online",
        desc="Sign in to BetItaly through betitaly.online. Recovery tips, 2FA habits and lobby checks. No fake forms. 18+.",
        keys="BetItaly login, BetItaly sign in, BetItaly account, betitaly.online",
        kicker="Login",
        h1="BetItaly Login",
        span="Official sign-in path via betitaly.online",
        lead="Reach BetItaly login from betitaly.online without mirror hopping. Use Play Now, enter credentials only on the live platform, then confirm your account name in the lobby.",
        cta="Open Login",
        cover="assets/pages/bi-login.jpg",
        cover_alt="BetItaly login cover",
        promo="promo-login.jpg",
        promo_alt="BetItaly login promo",
        badge="LOGIN",
        pk="BetItaly lobby door",
        pt="Sign in, then open calcio odds or slots",
        ps="No password fields on this hub — continue to the live BetItaly login.",
        essay=(
            "Login is a short walk: leave betitaly.online through Play Now, land on BetItaly, type the password only there. If the URL looks off, stop.",
            "After the header shows your name, you can move to Serie A odds, The Dog House or JetX without opening a second account. Keep 2FA on when the live site offers it.",
        ),
        chapters=[
            ("BetItaly login basics", "Use betitaly.online to reach the live BetItaly lobby without hunting random mirrors.", "Open Play Now, land on BetItaly, then keep one bookmark for return visits."),
            ("Account readiness", "Finish profile details early so KYC does not stall cashouts later.", "Use a password manager and enable 2FA when the platform offers it."),
            ("Session discipline", "Set a bankroll and a stop time before you open calcio markets or games.", "Close the session when either limit hits — do not chase."),
            ("Product path", "Login sits alongside slots, crash, live tables and calcio odds inside one BetItaly account.", "Jump from this hub with Play Now only — no fake forms here."),
            ("Mobile vs desktop", "One login works on phone and desktop browsers for BetItaly.", "Prefer a private device and stable connection for cashier steps."),
            ("Payments awareness", "Deposit with methods you also control for withdrawals.", "Keep billing name aligned with your BetItaly profile."),
            ("Support habits", "Save transaction IDs before contacting support.", "Use in-platform help after login for account-specific issues."),
            ("Session limits", "Set deposit caps and cool-offs inside BetItaly if you need tighter control.", "Stop when play stops feeling recreational."),
            ("Return path", "Bookmark betitaly.online so you always re-enter BetItaly from a known URL.", "Recheck the address bar after redirects before entering credentials."),
        ],
        faq=[
            ("How do I open BetItaly from betitaly.online?", "Tap Play Now on betitaly.online, follow through to the live BetItaly site, then complete login there."),
            ("Are there fake login forms here?", "No. Never enter passwords on this hub. Credentials belong only on the live BetItaly site."),
            ("What if I forget the BetItaly password?", "Use the official recovery link on the live login page. Do not type reset details on the hub."),
            ("Should I enable 2FA on BetItaly?", "Yes, when the platform offers it. Pair it with a password manager."),
            ("Where do I manage limits on BetItaly?", "Use deposit limits, reality checks and cool-offs inside the logged-in BetItaly account tools."),
        ],
    ),
    dict(
        slug="bi-join.html",
        nav="Register",
        title="BetItaly Register | betitaly.online",
        desc="Create a BetItaly account via betitaly.online. One profile for Serie A odds, slots and cashier. KYC early. 18+.",
        keys="BetItaly register, BetItaly signup, BetItaly account, betitaly.online",
        kicker="Register",
        h1="BetItaly Register",
        span="Create your account through betitaly.online",
        lead="Join BetItaly from betitaly.online with Play Now. Finish profile details early so calcio odds, The Dog House and cashier sit in one verified account.",
        cta="Create Account",
        cover="assets/pages/bi-join.jpg",
        cover_alt="BetItaly register cover",
        promo="promo-join.jpg",
        promo_alt="BetItaly register promo",
        badge="JOIN",
        pk="BetItaly signup desk",
        pt="One profile for calcio and casino",
        ps="Finish KYC early, then open The Dog House or Serie A boards.",
        essay=(
            "Registration is one ticket: open Play Now, create the BetItaly profile on the live site, then confirm email if asked. This hub never hosts a signup form.",
            "After the account exists, calcio odds and slots share the same wallet. Complete KYC before a busy Serie A weekend so withdrawals do not stall.",
        ),
        chapters=[
            ("Why join from this hub", "betitaly.online keeps a clean path to the live BetItaly signup.", "Skip random mirrors and bookmark the hub after you join."),
            ("Details that matter", "Use your real name as it appears on payment methods.", "A mismatch later slows cashier reviews."),
            ("Calcio first habit", "After signup, open Serie A boards before chasing slot bonuses.", "Write a stake size for the first weekend."),
            ("Bonus readiness", "Read wagering before you claim any welcome offer.", "Eligible calcio markets and slots are listed on the live site."),
            ("KYC early", "Upload documents when BetItaly asks — do not wait for a cashout.", "Keep photos sharp and uncropped."),
            ("Device choice", "Register on a private phone or desktop, not a shared cafe PC.", "Save the password in a manager."),
            ("Same wallet", "Slots, JetX and live tables use the same BetItaly balance as calcio.", "Do not open a second profile."),
            ("Limits", "Set a deposit cap on day one if weekend calcio tempts overspend.", "Cool-off tools sit in account settings."),
            ("Return visits", "Come back through betitaly.online, then Play Now.", "Confirm the live URL before you type the new password."),
        ],
        faq=[
            ("How do I register on BetItaly?", "Tap Play Now from betitaly.online and complete signup only on the live BetItaly site."),
            ("Do I need a new account for slots?", "No. One BetItaly profile covers calcio odds, slots, crash, live tables and cashier."),
            ("When should I complete KYC?", "As soon as the live site asks — ideally before your first withdrawal."),
            ("Can I register on mobile?", "Yes. The same Play Now path works in a phone browser."),
            ("Are there signup forms on this hub?", "No. Never enter personal data on betitaly.online itself."),
        ],
    ),
    dict(
        slug="bi-bonus.html",
        nav="Bonus",
        title="BetItaly Welcome Bonus | betitaly.online",
        desc="Read BetItaly wagering, eligible calcio and slots before you claim. No invented percentages on this hub. 18+.",
        keys="BetItaly bonus, BetItaly welcome bonus, BetItaly wagering, betitaly.online",
        kicker="Bonus",
        h1="BetItaly Welcome Bonus",
        span="Registration path and wagering basics",
        lead="Open the BetItaly welcome path from betitaly.online only after you can name the wagering rule. Eligible Serie A markets and slots sit on the live offer page — this hub never invents a percent.",
        cta="Claim Bonus",
        cover="assets/pages/bi-bonus.jpg",
        cover_alt="BetItaly bonus cover",
        promo="promo-bonus.jpg",
        promo_alt="BetItaly bonus promo",
        badge="BONUS",
        pk="BetItaly welcome path",
        pt="Read wagering before you claim",
        ps="Eligible calcio and slots sit in one account after signup. Continue via Play Now.",
        essay=(
            "A bonus is useful only when you already know the wagering multiple, the expiry and whether JetX counts. If a number is missing on the live page, do not guess from this hub.",
            "Claim after login, keep a written stake plan for Serie A, and separate bonus funds from crash rounds if terms exclude them.",
        ),
        chapters=[
            ("Read first", "Open the live BetItaly offer after Play Now.", "Write down wagering, min odds and expiry before you deposit."),
            ("Calcio eligibility", "Check which Serie A markets count toward wagering.", "Live extras and player props may sit outside the rule."),
            ("Slots that count", "The Dog House or Wolf Gold may count at different weights.", "Search the title after login and confirm the contribution."),
            ("Crash caution", "JetX and Aviator are often excluded or weighted low.", "Do not assume crash clears a welcome offer."),
            ("One account", "Bonus, calcio and cashier share the same BetItaly profile.", "Do not create a second account to chase another gift."),
            ("KYC and bonus", "Identity checks can pause bonus funds as well as cashouts.", "Finish documents early."),
            ("Time limits", "Expiry clocks start when you claim, not when you plan to play.", "Set a calendar reminder."),
            ("Stop rules", "A bonus is not a reason to raise stakes after a loss.", "Keep the same bankroll you wrote before signup."),
            ("Support", "Ask live chat for the current terms after login.", "Save the chat transcript with the offer name."),
        ],
        faq=[
            ("Does this hub list a BetItaly bonus percent?", "No. Percentages belong on the live BetItaly offer page only."),
            ("Can I use a bonus on Serie A?", "Only if the live terms list calcio markets and a minimum odds rule."),
            ("Do slots clear wagering faster?", "Weighting differs by title. Confirm The Dog House or Wolf Gold on the live page."),
            ("What if JetX is excluded?", "Keep bonus funds off crash rounds until terms say otherwise."),
            ("How do I claim?", "Play Now from betitaly.online, log in, then open the official promotions desk."),
        ],
    ),
    dict(
        slug="bi-slots.html",
        nav="Slots",
        title="BetItaly Slots: The Dog House, Wolf Gold & More | betitaly.online",
        desc="Search The Dog House, Wolf Gold, Wild West Gold, Great Rhino, Buffalo King and Cleopatra after BetItaly login. 18+.",
        keys="BetItaly slots, The Dog House, Wolf Gold, Wild West Gold, Cleopatra, betitaly.online",
        kicker="Slots",
        h1="BetItaly Top Slots",
        span="The Dog House and world titles via betitaly.online",
        lead="Jump into BetItaly slots from betitaly.online. Featured titles stay in the global top tier — set a spin budget before you load the first reel.",
        cta="Open Slots",
        cover="assets/pages/bi-slots.jpg",
        cover_alt="BetItaly slots cover",
        promo="promo-slots.jpg",
        promo_alt="BetItaly slots promo",
        badge="SLOTS",
        pk="BetItaly reel hall",
        pt="World-famous reels after login",
        ps="The Dog House, Wolf Gold and Cleopatra — search, then spin inside BetItaly.",
        extra_grid="slots",
        essay=(
            "Treat the BetItaly slot hall like a matchday squad list: one title, one budget, one stop time. The Dog House and Wolf Gold reward patience more than rapid clicks.",
            "Wild West Gold and Great Rhino move differently. Buffalo King and Cleopatra sit in the same lobby. Open Play Now, search the exact name, then spin only after the cashier is funded on purpose.",
        ),
        chapters=[
            ("Search exact titles", "Type The Dog House or Wolf Gold in the live lobby search.", "Avoid lookalike names that are not the original game."),
            ("Budget first", "Decide a spin size before the first reel stops.", "Stop when the number is gone."),
            ("Volatility", "Wild West Gold and Buffalo King can swing harder than Fruit Party.", "Do not raise stakes to chase a dry stretch."),
            ("Providers", "Pragmatic Play titles sit beside Play'n GO and NetEnt in the same account.", "Open the provider strip on this hub, then continue via Play Now."),
            ("Bonus weights", "Some welcome offers weight slots differently.", "Read the live contribution table."),
            ("Session length", "Set a clock as well as a cash limit.", "Leave the hall when either hits."),
            ("Mobile reels", "The same titles load in a phone browser after login.", "Prefer Wi-Fi for heavier games."),
            ("Calcio pause", "You can leave a slot and open Serie A odds without a new account.", "Keep one wallet."),
            ("Show more", "The three Show more buttons continue to the live BetItaly lobby.", "They are not extra fake grids on this hub."),
        ],
        faq=[
            ("Which slots should I search first?", "The Dog House, Wolf Gold, Wild West Gold, Great Rhino, Buffalo King and Cleopatra."),
            ("Are these real world titles?", "Yes. They are popular studio games, not invented hub names."),
            ("Can I play slots and calcio on one account?", "Yes. One BetItaly profile covers both."),
            ("Do I need a separate slots deposit?", "No. Use the same cashier after login."),
            ("Where do I find more titles?", "Tap Show more to continue into the live BetItaly lobby."),
        ],
    ),
    dict(
        slug="bi-odds.html",
        nav="Odds",
        title="BetItaly Sports Odds: Serie A & Calcio | betitaly.online",
        desc="BetItaly calcio odds for Serie A, Coppa and Champions League. Sample 1X2 boards, then bet on the live sportsbook. 18+.",
        keys="BetItaly odds, BetItaly Serie A, BetItaly calcio, Champions League, betitaly.online",
        kicker="Odds",
        h1="BetItaly Sports Odds",
        span="Serie A 1X2, live markets and major leagues",
        lead="Use betitaly.online to reach BetItaly login, then open calcio odds first. Slots, JetX crash and live casino stay one click away in the same profile.",
        cta="View Odds",
        cover="assets/pages/bi-odds.jpg",
        cover_alt="BetItaly odds cover",
        promo="promo-odds.jpg",
        promo_alt="BetItaly odds promo",
        badge="ODDS",
        pk="BetItaly calcio boards",
        pt="Lock Serie A 1X2 before kick-off",
        ps="Derby d'Italia and Coppa markets — compare, then bet inside BetItaly.",
        extra_grid="odds",
        essay=(
            "Calcio comes first on BetItaly: Derby d'Italia, the Olimpico derby and midweek Serie A kick-offs. The boards on this hub are samples — live prices move on the sportsbook.",
            "Size 1X2 stakes to a written bankroll. Handicaps and totals sit behind login. Do not chase a red card swing with money you planned for Sunday.",
        ),
        chapters=[
            ("Serie A first", "Start with Inter, Juventus, Milan, Napoli, Roma and Lazio boards.", "Compare 1X2, then open the live line."),
            ("Bankroll", "Write a weekend limit before you tap Place Bet.", "Split it across two or three matches, not one longshot."),
            ("Live markets", "In-play calcio moves faster than pre-match.", "If you cannot watch the game, skip live extras."),
            ("Other leagues", "Premier League, La Liga and Bundesliga sit next to Serie A.", "Same wallet, same login."),
            ("Accas", "Multiples look generous and break often.", "Keep them small versus singles."),
            ("Cashier before kick-off", "Deposit early so a pending method does not miss the whistle.", "Use a method you also control for withdrawals."),
            ("Limits", "Use account limits if Saturday calcio stacks too many kick-offs.", "A pause is cheaper than a chase."),
            ("Same profile", "After a match you can open The Dog House without a second signup.", "One BetItaly account."),
            ("Return path", "Bookmark betitaly.online for the next matchday.", "Play Now still lands on the live sportsbook."),
        ],
        faq=[
            ("Are the 1X2 numbers live?", "They are orientation samples. Place the bet on the live BetItaly sportsbook."),
            ("Which league is first?", "Serie A and Italian derbies lead this hub, then Champions League and other top leagues."),
            ("Can I bet calcio and slots together?", "Yes, after one login. Keep separate session budgets."),
            ("What does Place Bet do?", "It continues to the live BetItaly offer — this hub does not take stakes."),
            ("How do I find more markets?", "Open Play Now for handicaps, totals, player props and in-play."),
        ],
    ),
    dict(
        slug="bi-crash.html",
        nav="Crash",
        title="BetItaly Crash: JetX, Aviator & Plinko | betitaly.online",
        desc="Open JetX, Aviator and Plinko at BetItaly via betitaly.online. Set auto cash-out before the round climbs. 18+.",
        keys="BetItaly crash, JetX, Aviator, Plinko, BetItaly Aviator, betitaly.online",
        kicker="Crash",
        h1="BetItaly Crash Games",
        span="JetX, Aviator and Plinko via betitaly.online",
        lead="Open JetX-style crash titles at BetItaly through betitaly.online. Decide auto cash-out rules before the round climbs.",
        cta="Open Crash",
        cover="assets/pages/bi-crash.jpg",
        cover_alt="BetItaly crash cover",
        promo="promo-crash.jpg",
        promo_alt="BetItaly crash promo",
        badge="CRASH",
        pk="BetItaly JetX desk",
        pt="Cash out on a written rule",
        ps="Decide auto cash-out before JetX, Aviator or Plinko starts climbing.",
        extra_grid="crash",
        essay=(
            "Crash rounds are short. Write the cash-out multiplier before JetX or Aviator leaves the ground. If you miss it, the next round is a new decision — not a recovery plan.",
            "Plinko and Mines need the same discipline with a different rhythm. Keep crash money away from a Serie A acca you still want to protect.",
        ),
        chapters=[
            ("JetX first", "Search JetX after login and set auto cash-out.", "Do not raise the target after a miss."),
            ("Aviator", "The same rule applies: write the exit before take-off.", "One account, same cashier as calcio."),
            ("Plinko", "Pick a risk row with a budget, not a whim.", "Stop when the stack is gone."),
            ("Spaceman and Lucky Jet", "They sit in the same crash row on this hub.", "Search the exact name in the live lobby."),
            ("Mines", "Reveal tiles only inside a pre-set click count.", "Do not add clicks after a scare."),
            ("Bonus terms", "Many offers exclude crash or weight it low.", "Read the live page before you mix bonus funds."),
            ("Time cap", "Ten minutes of crash can outspend an hour of slots.", "Use a clock."),
            ("Calcio break", "You can leave crash and open Serie A without a new login.", "Keep wallets mentally split."),
            ("Show more", "Continue to the live BetItaly crash list via Show more.", "This hub is orientation, not a game client."),
        ],
        faq=[
            ("What crash games are featured?", "JetX, Aviator, Plinko, plus Spaceman, Lucky Jet and Mines."),
            ("Should I use auto cash-out?", "Yes. Set it before the round starts."),
            ("Can I play crash after a Serie A bet?", "Yes, same BetItaly account. Use a separate cash slice."),
            ("Does a welcome bonus apply to JetX?", "Only if the live terms say so."),
            ("Where do I open the real game?", "Play Now or Show more from betitaly.online."),
        ],
    ),
    dict(
        slug="bi-live.html",
        nav="Live",
        title="BetItaly Live Casino: Lightning Roulette & Crazy Time | betitaly.online",
        desc="Open Lightning Roulette, Crazy Time and Blackjack at BetItaly via betitaly.online. Studio tables after login. 18+.",
        keys="BetItaly live casino, Lightning Roulette, Crazy Time, Blackjack, betitaly.online",
        kicker="Live",
        h1="BetItaly Live Casino",
        span="Lightning Roulette and studio tables via betitaly.online",
        lead="Open BetItaly from betitaly.online when you want live game-show tables ready after login. Slots, crash and calcio odds stay in the same lobby.",
        cta="Open Live",
        cover="assets/pages/bi-live.jpg",
        cover_alt="BetItaly live casino cover",
        promo="promo-live.jpg",
        promo_alt="BetItaly live promo",
        badge="LIVE",
        pk="BetItaly studio floor",
        pt="Lightning Roulette after a clean login",
        ps="Crazy Time and Blackjack share the same BetItaly account as calcio odds.",
        extra_grid="live",
        essay=(
            "Live tables run on studio time, not on your Saturday kick-off. Lightning Roulette and Crazy Time can outlast a Serie A first half — set a clock before you sit.",
            "Blackjack and Baccarat need a seat plan and a chip size. One BetItaly login covers the studio and the calcio board.",
        ),
        chapters=[
            ("Lightning Roulette", "Search the exact Evolution title after login.", "Decide a spin budget before the first lightning strike."),
            ("Crazy Time", "Game-show extras stretch sessions.", "Cap both time and chips."),
            ("Blackjack", "One table, one unit size.", "Do not add seats to chase."),
            ("Mega Wheel and Dream Catcher", "Wheel games feel light and spend fast.", "Keep them inside the live budget."),
            ("Baccarat", "Side bets are optional, not required.", "Main bets stay simpler to track."),
            ("Same cashier", "Studio chips come from the same wallet as Serie A.", "Do not treat live as house money."),
            ("Connection", "Prefer a stable network for video tables.", "If the stream lags, sit out the round."),
            ("Calcio overlap", "A live match and a live wheel at once splits attention.", "Pick one focus."),
            ("Show more", "The buttons continue to the live BetItaly lobby.", "No extra invented tables on this hub."),
        ],
        faq=[
            ("Which live games are listed?", "Lightning Roulette, Crazy Time, Blackjack, Mega Wheel, Baccarat and Dream Catcher."),
            ("Is this a live dealer client?", "No. This hub orients you; Play Now opens the live BetItaly studio."),
            ("Can I use one account for live and calcio?", "Yes."),
            ("Should I play live on mobile?", "Yes if the connection is stable. Log out on shared phones."),
            ("Do bonuses count on live tables?", "Check the live wagering table after login."),
        ],
    ),
    dict(
        slug="bi-app.html",
        nav="App",
        title="BetItaly Mobile App Path | betitaly.online",
        desc="Use BetItaly on your phone via betitaly.online. One account for Serie A odds, slots and cashier. 18+.",
        keys="BetItaly app, BetItaly mobile, BetItaly phone, betitaly.online",
        kicker="App",
        h1="BetItaly Mobile App Path",
        span="One account on phone and desktop",
        lead="Carry BetItaly in your pocket from betitaly.online. Bookmark the hub, tap Play Now, then stay on the live site for calcio odds and cashier.",
        cta="Open App",
        cover="assets/pages/bi-app.jpg",
        cover_alt="BetItaly mobile cover",
        promo="promo-app.jpg",
        promo_alt="BetItaly app promo",
        badge="APP",
        pk="BetItaly in your pocket",
        pt="Same lobby on a smaller screen",
        ps="Bookmark betitaly.online, tap Play Now, then stay on the live site.",
        essay=(
            "Mobile BetItaly is the same account as desktop. You do not need a second signup to check a Serie A price on the train.",
            "Prefer a private device for cashier steps. After a deposit, log out if you share the phone.",
        ),
        chapters=[
            ("Browser path", "Open betitaly.online, tap Play Now, then login on the live site.", "Add the hub to your home screen if you want a shortcut."),
            ("One profile", "Calcio, The Dog House and JetX stay in the same wallet.", "Do not create a mobile-only account."),
            ("Data and Wi-Fi", "Live tables want a stable link.", "If the stream drops, wait — do not mash extra chips."),
            ("Notifications", "Match alerts belong to the live platform settings.", "This hub does not send push spam."),
            ("Cashier on mobile", "Use a method you also control on desktop withdrawals.", "Complete KYC with readable photos."),
            ("Shared phones", "Log out after cashier.", "Never save a password in a borrowed browser."),
            ("Orientation", "Rotate only if the live lobby asks for landscape.", "Keep stakes visible."),
            ("Return", "Re-enter through betitaly.online so you skip random links.", "Check the address bar."),
            ("Help", "If a mobile page fails, retry on desktop or open Help.", "Save a screenshot and time for support."),
        ],
        faq=[
            ("Is there a separate BetItaly app store listing on this hub?", "This hub points you to the live platform via Play Now. Use the official path after login."),
            ("Does mobile use another account?", "No. One BetItaly login works on phone and desktop."),
            ("Can I bet Serie A on a phone?", "Yes, after login on the live sportsbook."),
            ("Is cashier safe on mobile?", "Use a private device, a stable connection and the same methods you control."),
            ("What if the page looks cropped?", "Rotate or zoom; the hub is built to keep lead and CTA visible on a 390-wide screen."),
        ],
    ),
    dict(
        slug="bi-pay.html",
        nav="Pay",
        title="BetItaly Payments | betitaly.online",
        desc="BetItaly cashier basics: deposit, withdraw and KYC. Use methods you control. 18+.",
        keys="BetItaly deposit, BetItaly withdraw, BetItaly cashier, BetItaly KYC, betitaly.online",
        kicker="Pay",
        h1="BetItaly Payments",
        span="Deposit, withdraw and KYC basics",
        lead="Fund BetItaly after login from betitaly.online. Deposit with a method you also control for withdrawals and finish KYC before a busy calcio weekend.",
        cta="Open Cashier",
        cover="assets/pages/bi-pay.jpg",
        cover_alt="BetItaly cashier cover",
        promo="promo-pay.jpg",
        promo_alt="BetItaly cashier promo",
        badge="PAY",
        pk="BetItaly cashier desk",
        pt="Deposit with a method you also control",
        ps="Complete KYC early so withdrawals do not stall after a winning week.",
        essay=(
            "The cashier is a sportsbook desk with chips, not a silent vault. Deposit only what you already planned for Serie A or a slot session.",
            "Withdrawals use the same methods when possible. Name on the profile should match the payment name.",
        ),
        chapters=[
            ("Login first", "There is no deposit form on this hub.", "Play Now, then open the live BetItaly cashier."),
            ("Method match", "Pay with cards or wallets you also own for cashouts.", "Third-party names trigger reviews."),
            ("KYC early", "Upload ID when asked, before you need a withdrawal.", "Clear photos beat cropped shots."),
            ("Calcio timing", "Fund before kick-off, not in the 89th minute.", "Pending deposits miss live lines."),
            ("Limits", "Daily deposit caps sit in account tools.", "Use them if weekend calcio stacks."),
            ("Bonus and cashier", "Some offers lock funds until wagering ends.", "Read the live note before you deposit into a bonus."),
            ("Failed payments", "Retry once, then contact live support with the time and method.", "Keep the reference ID."),
            ("Shared devices", "Never leave the cashier open on a borrowed phone.", "Log out."),
            ("Help", "Payment questions belong on the live site after login.", "This hub only orients you."),
        ],
        faq=[
            ("Can I deposit on this hub?", "No. Cashier lives on the live BetItaly site after Play Now."),
            ("When should I do KYC?", "As soon as the platform asks — ideally before your first cashout."),
            ("Which method should I use?", "One you personally control and can also use to withdraw."),
            ("Why is a withdrawal pending?", "Name mismatch, unfinished KYC or bonus locks are common reasons — check the live cashier."),
            ("Does calcio need a separate wallet?", "No. One BetItaly cashier covers odds, slots, crash and live."),
        ],
    ),
    dict(
        slug="bi-help.html",
        nav="Help",
        title="BetItaly Help | betitaly.online",
        desc="BetItaly support habits: transaction IDs, recovery on the live login, session tools. 18+.",
        keys="BetItaly help, BetItaly support, BetItaly contact, betitaly.online",
        kicker="Help",
        h1="BetItaly Help",
        span="Support habits and session tools",
        lead="Ask inside the live BetItaly lobby after you leave betitaly.online via Play Now. Bring transaction IDs. Password resets stay on the official login page.",
        cta="Get Help",
        cover="assets/pages/bi-help.jpg",
        cover_alt="BetItaly help cover",
        promo="promo-help.jpg",
        promo_alt="BetItaly help promo",
        badge="HELP",
        pk="BetItaly support floor",
        pt="Ask inside the live lobby",
        ps="Bring transaction IDs. Password resets stay on the official login page.",
        essay=(
            "This hub cannot reset a password or move a withdrawal. Those tools sit on the live BetItaly site after login.",
            "Before you write to support, save the time, method and reference. Responsible play tools also live in the logged-in account, not on this page.",
        ),
        chapters=[
            ("Live chat", "Open Play Now, log in, then use in-platform help.", "Paste IDs, do not retype from memory."),
            ("Password", "Use the official forgot-password link on the live login.", "Never send a password to anyone."),
            ("Payments", "Cashier tickets need method, amount and time.", "Screenshots help."),
            ("Bonuses", "Quote the offer name as shown after login.", "This hub does not invent percents."),
            ("Limits", "Deposit caps, reality checks and cool-offs are account tools.", "Use them if calcio weekends run long."),
            ("18+", "BetItaly is for adults only.", "If play stops feeling recreational, stop."),
            ("Mirrors", "Return through betitaly.online so you skip random links.", "Check the address bar."),
            ("Mobile issues", "Retry on desktop if a live table will not load.", "Note the device and browser."),
            ("Self-exclude", "If you need a hard stop, use the live account tools.", "Support can point to the official path after login."),
        ],
        faq=[
            ("Can you reset my BetItaly password here?", "No. Use the official recovery link on the live login page."),
            ("Where is real support?", "Inside the live BetItaly lobby after Play Now."),
            ("What should I send to support?", "Transaction IDs, time, method and a short description — never your password."),
            ("How do I set limits?", "Open account tools after login on the live site."),
            ("Is this hub official support?", "It is an orientation hub. Account actions happen on the live platform."),
        ],
    ),
]

SLOTS = [
    ("the-dog-house.jpg", "The Dog House"),
    ("wolf-gold.jpg", "Wolf Gold"),
    ("wild-west-gold.jpg", "Wild West Gold"),
    ("great-rhino.jpg", "Great Rhino"),
    ("buffalo-king.jpg", "Buffalo King"),
    ("cleopatra.jpg", "Cleopatra"),
    ("fruit-party.jpg", "Fruit Party"),
    ("big-bass-bonanza.jpg", "Big Bass Bonanza"),
    ("wisdom-of-athena.jpg", "Wisdom of Athena"),
    ("starlight-princess.jpg", "Starlight Princess"),
]
CRASH = [
    ("jetx.jpg", "JetX"),
    ("aviator.jpg", "Aviator"),
    ("plinko.jpg", "Plinko"),
    ("spaceman.jpg", "Spaceman"),
    ("lucky-jet.jpg", "Lucky Jet"),
    ("mines.jpg", "Mines"),
]
LIVE = [
    ("lightning-roulette.jpg", "Lightning Roulette"),
    ("crazy-time.jpg", "Crazy Time"),
    ("blackjack.jpg", "Blackjack"),
    ("mega-wheel.jpg", "Mega Wheel"),
    ("baccarat.jpg", "Baccarat"),
    ("dream-catcher.jpg", "Dream Catcher"),
]

ODDS_ROWS = [
    ("Serie A · Derby d'Italia", "INT", "Inter", "JUV", "Juventus", "2.20", "3.25", "3.40"),
    ("Serie A · San Siro", "ACM", "AC Milan", "NAP", "Napoli", "2.35", "3.20", "3.15"),
    ("Serie A · Olimpico", "ROM", "Roma", "LAZ", "Lazio", "2.45", "3.15", "3.05"),
    ("Serie A · Bergamo", "ATA", "Atalanta", "FIO", "Fiorentina", "1.95", "3.50", "3.90"),
    ("Champions League · Knockout", "INT", "Inter", "RMA", "Real Madrid", "2.85", "3.35", "2.45"),
    ("Premier League · Midweek", "LIV", "Liverpool", "ARS", "Arsenal", "2.28", "3.40", "3.05"),
]


def hreflang(slug):
    rows = []
    for lg in LANGS:
        href = f"https://betitaly.online/{slug}?lang={lg}"
        rows.append(f'<link rel="alternate" hreflang="{lg}" href="{href}">')
    rows.append(f'<link rel="alternate" hreflang="x-default" href="https://betitaly.online/{slug}">')
    return "\n".join(rows)


def nav_html(active):
    bits = []
    for href, label in NAV:
        cls = "nav-link is-active" if label == active else "nav-link"
        bits.append(f'<a class="{cls}" href="{href}">{label}</a>')
    return "".join(bits)


def cards(items, folder, tag, klass="card-grid"):
    out = [f'<div class="{klass}">']
    for fn, title in items:
        out.append(
            f'<article class="game-card"><a href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">'
            f'<img src="/assets/{folder}/{fn}" alt="{title}" width="720" height="540" loading="lazy">'
            f'<div class="card-meta"><div class="tag">{tag}</div><h3>{title}</h3></div></a></article>'
        )
    out.append("</div>")
    out.append(
        f'<div class="grid-more trio"><a class="btn btn-ghost" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">Show more</a>'
        f'<a class="btn btn-ghost" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">Show more</a>'
        f'<a class="btn btn-ghost" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">Show more</a></div>'
    )
    return "".join(out)


def odds_board():
    rows = []
    for meta, a, an, b, bn, o1, ox, o2 in ODDS_ROWS:
        rows.append(
            f'<article class="odds-row"><div><div class="odds-meta">{meta}</div><div class="odds-match">'
            f'<span class="team"><span class="team-badge">{a}</span><span class="team-name">{an}</span></span>'
            f'<span class="odds-vs">VS</span>'
            f'<span class="team"><span class="team-badge">{b}</span><span class="team-name">{bn}</span></span>'
            f'</div></div><div class="odds-prices"><div class="price"><small>1</small>{o1}</div>'
            f'<div class="price"><small>X</small>{ox}</div><div class="price"><small>2</small>{o2}</div></div>'
            f'<a class="btn btn-accent" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">Place Bet</a></article>'
        )
    sports = (
        f'<nav class="odds-sports" aria-label="Sports markets">'
        f'<a class="odds-sport is-active" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">Football</a>'
        f'<a class="odds-sport" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">Basketball</a>'
        f'<a class="odds-sport" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">Tennis</a>'
        f'<a class="odds-sport" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">Ice Hockey</a>'
        f'<a class="odds-sport" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">Esports</a>'
        f'<a class="odds-sport" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">MMA</a></nav>'
    )
    return sports + '<div class="odds-board">' + "".join(rows) + "</div>"


def extra(kind):
    if kind == "slots":
        return cards(SLOTS, "slots", "Slot")
    if kind == "crash":
        return cards(CRASH, "crash", "Crash", "card-grid six")
    if kind == "live":
        return cards(LIVE, "live", "Live", "card-grid six")
    if kind == "odds":
        return odds_board()
    return ""


def faq_json(p):
    ents = []
    for q, a in p["faq"]:
        ents.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
    import json
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "url": f"https://betitaly.online/{p['slug']}", "mainEntity": ents}, ensure_ascii=False)


def page_html(p):
    ch = []
    for i, (t, a, b) in enumerate(p["chapters"], 1):
        ch.append(f'<article class="chapter"><div class="chapter-n">{i:02d}</div><h3>{t}</h3><p>{a}</p><p>{b}</p></article>')
    fq = []
    for q, a in p["faq"]:
        fq.append(f'<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>')
    grid = extra(p.get("extra_grid"))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<meta name="keywords" content="{p['keys']}">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="https://betitaly.online/{p['slug']}">
{hreflang(p['slug'])}
<meta property="og:type" content="website">
<meta property="og:site_name" content="BetItaly">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:url" content="https://betitaly.online/{p['slug']}">
<meta property="og:image" content="https://betitaly.online/assets/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico?v=bi1" sizes="any">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png?v=bi1">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=bi1">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@1,600;1,800&family=DM+Sans:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/pitch.css?v=bi1">
<link rel="stylesheet" href="/css/i18n.css?v=bi1">
<script type="application/ld+json">{faq_json(p)}</script>
</head>
<body class="page">
<div class="tri-strip" aria-hidden="true"><span></span><span></span><span></span></div>
<header class="pitch-head" id="siteHeader">
<div class="wrap header-bar">
<a class="brand" href="/" aria-label="BetItaly home"><span class="brand-mark"><img src="/assets/brand/logo.png" alt="BetItaly logo" width="46" height="46"></span><span class="brand-copy"><span class="brand-name"><i>Bet</i>Italy</span><span class="brand-tag">Official</span></span></a>
<button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="siteNav" type="button" aria-label="Open menu"><span></span><span></span><span></span></button>
<nav class="site-nav" id="siteNav" aria-label="Primary">{nav_html(p['nav'])}</nav>
<div class="header-actions"><div class="lang-switch" id="langSwitch"><button type="button" class="lang-switch-btn" aria-haspopup="listbox" aria-expanded="false" aria-label="Language"><img class="lang-flag-img" src="https://flagcdn.com/w40/gb.png" width="22" height="16" alt="English flag" loading="lazy" decoding="async"><span class="lang-code">EN</span><span class="lang-name" data-i18n-skip="1">English</span></button><div class="lang-switch-panel" role="listbox"></div></div><a class="btn btn-accent header-cta" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">Play Now</a></div>
</div>
</header>
<section class="page-hero"><div class="wrap"><div class="page-hero-shell">
<div>
<p class="kicker">{p['kicker']}</p>
<h1>{p['h1']}<span>{p['span']}</span></h1>
<p class="lead">{p['lead']}</p>
<div class="cta-row">
<a class="btn btn-accent" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">{p['cta']}</a>
<a class="btn btn-ghost" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">Play Now</a>
</div>
</div>
<div class="page-cover"><img src="/{p['cover']}" alt="{p['cover_alt']}" width="1100" height="825" loading="eager"></div>
</div></div></section>
<div class="wrap"><a class="promo-fx" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank"><span class="promo-badge">{p['badge']}</span><div class="promo-media"><img src="/assets/promo/{p['promo']}" alt="{p['promo_alt']}" width="1600" height="900" loading="lazy"></div><div class="promo-copy"><span class="promo-kicker">{p['pk']}</span><div class="promo-title">{p['pt']}</div><p class="promo-sub">{p['ps']}</p></div><span class="promo-cta">{p['cta']}</span></a></div>
<section class="wrap"><div class="essay">
<p>{p['essay'][0]}</p>
<p>{p['essay'][1]}</p>
</div></section>
<section class="wrap">{grid}</section>
<section class="chapters wrap"><div class="section-head"><h2>Guide chapters</h2><p class="mute">Practical steps for players.</p></div>
<div class="chapter-grid">{''.join(ch)}</div></section>
<section class="faq wrap"><div class="section-head"><h2>FAQ</h2><p class="mute">Straight answers for login, bonus, odds, slots, crash and cashier.</p></div>
<div class="faq-list">{''.join(fq)}</div></section>
<section class="cta-band"><div class="wrap">
<h2>Ready for BetItaly?</h2>
<p class="mute">Official path to lobby, calcio odds, slots, crash and live tables.</p>
<div class="cta-row">
<a class="btn btn-accent" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">Open Login</a>
<a class="btn btn-ghost" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">Play Now</a>
</div>
</div></section>
<footer class="site-footer">
<div class="wrap footer-grid">
<div>
<div class="footer-brand" data-i18n-skip="1">BetItaly</div>
<p class="mute">Hub for login, calcio odds, slots, crash, live casino and cashier on betitaly.online.</p>
<a class="btn btn-accent" href="{OFFER}" rel="nofollow sponsored noopener" target="_blank">Play Now</a>
</div>
<div class="footer-links">
<a href="/bi-login.html">Login</a>
<a href="/bi-join.html">Register</a>
<a href="/bi-bonus.html">Bonus</a>
<a href="/bi-slots.html">Slots</a>
<a href="/bi-odds.html">Sports Odds</a>
<a href="/bi-crash.html">Crash</a>
<a href="/bi-live.html">Live Casino</a>
<a href="/bi-app.html">App</a>
<a href="/bi-pay.html">Payments</a>
<a href="/bi-help.html">Help</a>
</div>
</div>
<div class="wrap footer-base"><span>&copy; 2026 BetItaly</span><span>Responsible play</span><span>18+</span></div>
</footer>
<script src="/js/pitch.js"></script>
<script src="/js/i18n-dict.js?v=bi1"></script>
<script src="/js/i18n-more.js?v=bi1"></script>
<script src="/js/i18n.js?v=bi1"></script>
</body>
</html>
"""


def main():
    for p in PAGES:
        (ROOT / p["slug"]).write_text(page_html(p), encoding="utf-8")
        print("wrote", p["slug"])


if __name__ == "__main__":
    main()
