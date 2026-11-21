import java.util.Arrays;
import java.util.HashSet;
import java.util.Locale;
import java.util.Set;

/** Dependency-free behavioral tests for the standalone exercise only. */
public final class UsernameGeneratorTest {
    private static int passed;

    public static void main(String[] args) {
        equal("smiller", generate("Sarah", "Miller", Set.of(), 20));
        equal("smiller3", generate("Sarah", "Miller", Set.of("SMILLER", "smiller2"), 20));
        equal("aoneil", generate("Ann", "O'Neil", Set.of(), 20));
        equal("bsmithjones", generate(" Bob ", " Smith-Jones ", Set.of(), 20));
        equal("mvanburen", generate("Mitch", "van Buren", Set.of(), 20));
        equal("smiller2", generate("Sarah", "Miller", Set.of(" smiller "), 20));
        rejects(() -> generate(null, "Miller", Set.of(), 20));
        rejects(() -> generate("Sarah", " ", Set.of(), 20));
        rejects(() -> generate("Élodie", "Miller", Set.of(), 20));
        rejects(() -> generate("Sarah", "M1ller", Set.of(), 20));
        rejects(() -> generate("Sarah", "Miller", Set.of(), 6));
        rejects(() -> generate("Sarah", "Miller", Set.of("smiller"), 7));
        rejects(() -> generate("Sarah", "Miller", null, 20));
        rejects(() -> generate("Sarah", "Miller", new HashSet<>(Arrays.asList((String) null)), 20));
        rejects(() -> generate("Sarah", "Miller", Set.of(), 1));
        rejects(() -> generate("Sarah", "Miller", Set.of(), 65));

        Set<String> occupied = new HashSet<>(Set.of("smiller"));
        equal("smiller2", generate("Sarah", "Miller", occupied, 20));
        if (!occupied.equals(Set.of("smiller"))) {
            throw new AssertionError("Input snapshot was mutated");
        }
        passed++;
        Locale previousLocale = Locale.getDefault();
        try {
            Locale.setDefault(Locale.forLanguageTag("tr-TR"));
            equal("imiller", generate("Ian", "MILLER", Set.of(), 20));
        } finally {
            Locale.setDefault(previousLocale);
        }
        System.out.println("Passed " + passed + " standalone Java checks; no IIQ integration tested.");
    }

    private static String generate(String first, String last, Set<String> occupied, int limit) {
        return UsernameGenerator.generate(first, last, occupied, limit);
    }

    private static void equal(String expected, String actual) {
        if (!expected.equals(actual)) {
            throw new AssertionError("Expected " + expected + " but got " + actual);
        }
        passed++;
    }

    private static void rejects(Runnable action) {
        try {
            action.run();
        } catch (IllegalArgumentException expected) {
            passed++;
            return;
        }
        throw new AssertionError("Expected input rejection");
    }
}
