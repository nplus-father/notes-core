export { withBase } from "./lib/url";
export { defineSite } from "./lib/site-config";
export type { SiteConfig, NavLink } from "./lib/site-config";
export { defineNoteCollections } from "./content";
export { bookUrl, siteUrl, siteLabel } from "./lib/links";
export {
  defineBibliography,
  defineSchools,
  defineProfile,
  shelfFromBibliography,
} from "./lib/library";
export type {
  BibliographyEntry,
  BibliographyStatus,
  School,
  SchoolFigure,
  AuthorProfile,
  Contribution,
  ReadingStage,
  Influence,
} from "./lib/library";
