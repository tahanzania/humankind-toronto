# humanKIND toronto website

A static site: plain HTML, CSS and JavaScript, with no build step and no framework. Everything that gets published lives in [`site/`](site/).

## Repo layout

```
.
├── README.md          ← you are here
├── .gitignore
├── docs/
│   └── website-copy.md    ← the client's copy document (contains internal editor notes)
└── site/              ← the deployable website (Cloudflare Pages output directory)
    ├── index.html, about.html, … (14 pages)
    ├── _redirects         ← 301s from the old Squarespace URLs
    ├── _headers           ← caching and security headers
    ├── sitemap.xml, robots.txt, favicon.png
    └── assets/
        ├── css/styles.css
        ├── js/main.js
        └── img/           ← optimized WebP photos and logos
```

> **Keep this repo private**, or remove `docs/` before making it public. The copy document contains internal editor comments (for example "SV: …") that were never meant for the public.

The original full-resolution photos (about 161 MB) are not in the repo. Keep them in Drive or Dropbox. The `.gitignore` excludes the local `hK website photo options` folder so they can't be committed by accident.

## Preview locally

```bash
cd site
python3 -m http.server 8000
# open http://localhost:8000
```

## Push to GitHub

```bash
# create an empty repo on github.com first (no README or .gitignore), then:
git add .
git commit -m "Initial site"
git branch -M main
git remote add origin git@github.com:<your-org>/<repo-name>.git
git push -u origin main
```

## Deploy on Cloudflare Pages

1. In the Cloudflare dashboard go to **Workers & Pages → Create → Pages → Connect to Git**, and pick this repo.
2. Use these build settings:

   | Setting | Value |
   | --- | --- |
   | Production branch | `main` |
   | Framework preset | `None` |
   | Build command | *(leave empty)* |
   | Build output directory | `site` |

3. Click **Save and Deploy**. The site goes live at `https://<project-name>.pages.dev`. Every push to `main` redeploys it, and every other branch gets its own preview URL.

### Before you point the real domain at it

- Review the `.pages.dev` site first. The real domain still points at Squarespace until you change DNS.
- The canonical URLs, social-preview tags, `sitemap.xml` and structured data already use `https://www.humankindtoronto.org`, so they are correct for launch. On the `.pages.dev` preview they intentionally point at the final domain.
- To go live, add the domain under your Pages project's **Custom domains** tab and follow Cloudflare's DNS instructions. Do this only when you're ready to replace the Squarespace site.
- After launch, open each old address once to confirm it redirects: `/on-site`, `/fundraising`, `/create-for-a-cause-2026`, `/covid19-1`. Then submit `https://www.humankindtoronto.org/sitemap.xml` in Google Search Console.

### How the URLs work on Cloudflare Pages

Cloudflare serves `about.html` at `/about` and redirects `/about.html` to `/about`. Canonical tags and the sitemap use the clean URLs. Internal links keep `.html` so the site also works when you open the files straight from disk, at the cost of one quick redirect per click.

## Contact form

The form opens the visitor's own email app with the message filled in, addressed to helpforhumankind@gmail.com, so no server is needed. To receive submissions directly instead, point the form at a form service such as Formspree or Basin (`#contact-form` in `site/contact.html`) and remove the `submit` handler at the bottom of `site/assets/js/main.js`. Cloudflare Pages has no built-in forms.

## Editing content

- The header and footer are repeated in every page. If you change them, update every `.html` file in `site/`.
- Photos are in `site/assets/img/` as WebP files, sized to 1400px on the longest edge. To add one, export it as WebP and include `width`, `height` and descriptive `alt` attributes on the `<img>` tag. If you replace an existing photo, give it a new filename, because images are cached for a year.
- Colours and fonts are CSS variables at the top of `site/assets/css/styles.css`.
- **After Nov 20, 2026:** update the event date on `create-for-a-cause.html`, the home page "Save the date" strip, the FAQ answer and the Event structured data. The countdown hides itself once the date passes.

## Pages

| File | Page |
| --- | --- |
| `index.html` | Home |
| `about.html` | Who We Are: values, mission and vision, team |
| `our-story.html` | History, 2017 to present |
| `programs.html` | Life Skills, Yoga & Cooking, Art Sessions, Shared Meals |
| `annual-drives.html` | Overview of the annual drives |
| `sock-drive.html`, `project-lunchbox.html`, `gift-of-hope.html` | One page per drive |
| `create-for-a-cause.html` | Annual fundraiser, with a countdown to Nov 20, 2026 |
| `volunteer.html` | Volunteer opportunities |
| `donate.html` | Embeds the existing donation form (glassregister.societ.com) |
| `faq.html` | FAQs, also marked up as FAQPage structured data |
| `contact.html` | Contact form |
| `404.html` | Not-found page |

## SEO already in place

- Unique `<title>` and meta description on every page
- Canonical link, plus Open Graph and Twitter card tags
- Structured data (JSON-LD): NGO organization, WebSite, BreadcrumbList on inner pages, FAQPage and Event
- Semantic HTML landmarks, one `<h1>` per page, descriptive alt text
- `sitemap.xml` and `robots.txt`
- Lazy-loaded images with explicit dimensions, so the layout doesn't shift while images load
