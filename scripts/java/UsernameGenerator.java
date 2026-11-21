import java.util.HashSet;
import java.util.Locale;
import java.util.Set;

/**
 * New standalone teaching exercise, not an IdentityIQ rule or deployed policy.
 * An intentionally narrow ASCII policy: first initial + full normalized surname,
 * followed by a numeric suffix when occupied. No network or directory writes.
 */
public final class UsernameGenerator {
    private UsernameGenerator() { }

    public static String generate(String firstName, String lastName,
                                  Set<String> occupiedNames, int maxLength) {
        if (maxLength < 2 || maxLength > 64) {
            throw new IllegalArgumentException("Maximum length must be 2 through 64");
        }
        String first = normalizeName(firstName);
        String last = normalizeName(lastName);
        if (occupiedNames == null) {
            throw new IllegalArgumentException("An occupied-name snapshot is required");
        }
        Set<String> occupied = new HashSet<>();
        for (String value : occupiedNames) {
            if (value == null || value.isBlank()) {
                throw new IllegalArgumentException("Occupied names must be nonblank");
            }
            occupied.add(value.trim().toLowerCase(Locale.ROOT));
        }
        String base = first.substring(0, 1) + last;
        if (base.length() > maxLength) {
            throw new IllegalArgumentException("Full surname exceeds naming policy length");
        }
        if (!occupied.contains(base)) {
            return base;
        }
        // At most n+1 suffix candidates are needed against n occupied names.
        for (long suffix = 2; suffix <= (long) occupied.size() + 2; suffix++) {
            String candidate = base + suffix;
            if (candidate.length() > maxLength) {
                throw new IllegalArgumentException("No suffix fits without truncating the surname");
            }
            if (!occupied.contains(candidate)) {
                return candidate;
            }
        }
        throw new IllegalStateException("No available candidate");
    }

    private static String normalizeName(String name) {
        if (name == null || name.isBlank()) {
            throw new IllegalArgumentException("First and last names are required");
        }
        String trimmed = name.trim();
        if (!trimmed.matches("[A-Za-z][A-Za-z '\\-]*")) {
            throw new IllegalArgumentException("Name requires manual review under this ASCII policy");
        }
        // This simplified policy removes ASCII spaces, apostrophes, and hyphens.
        return trimmed.replace(" ", "").replace("'", "").replace("-", "")
                .toLowerCase(Locale.ROOT);
    }
}
