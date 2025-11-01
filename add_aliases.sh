#!/bin/bash
# Add convenient aliases for road checking

ALIAS_FILE="$HOME/.bash_aliases"

echo "Adding road check aliases to $ALIAS_FILE"

# Create .bash_aliases if it doesn't exist
touch "$ALIAS_FILE"

# Add aliases if they don't already exist
if ! grep -q "alias roadcheck=" "$ALIAS_FILE" 2>/dev/null; then
    cat >> "$ALIAS_FILE" << 'EOF'

# Road closure checking aliases
alias roadcheck='python3 /home/homeassistant/test_roads.py'
alias roads='python3 /home/homeassistant/test_roads.py'
alias lummicheck='python3 /home/homeassistant/test_roads.py "Marine Drive" "Slater Road" "Haxton Way" "Ferndale Road" "Imhoff Road"'

EOF
    echo "✓ Aliases added!"
else
    echo "! Aliases already exist, skipping..."
fi

echo ""
echo "Reload your shell or run: source ~/.bash_aliases"
echo ""
echo "Then use:"
echo "  roadcheck \"Lummi Shore\"         # Check any road"
echo "  roads \"Marine Drive\" \"Slater\"   # Check multiple"
echo "  lummicheck                       # Check all Lummi access roads"
