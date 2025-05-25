"""A module for Aguglani-GA specific warnings."""
#  This file is part of Aguglani_CS23 : A framework for rapid Overall Aircraft Design
#  Copyright (C) 2022  Aguglani & ISAE-Aguglani-avi
#  Aguglani is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


class AguglaniGAWarning(UserWarning):
    """Base class for Aguglani-GA warning."""

    name = "warn_Aguglani_ga"


class VariableDescriptionWarning(AguglaniGAWarning):
    """Warning class for warnings in the generation of variable_descriptions.txt"""

    name = "warn_variable_descriptions"
