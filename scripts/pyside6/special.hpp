static const char msgInvalidParameterAdd[] =
    "Invalid parameter None passed to addLayoutOwnership().";

#ifndef _RETRIEVEOBJECTNAME_
#define _RETRIEVEOBJECTNAME_ // Guard for jumbo builds
static QByteArray retrieveObjectName(PyObject *obj)
{
    Shiboken::AutoDecRef objName(PyObject_Str(obj));
    return Shiboken::String::toCString(objName);
}
#endif
inline void addLayoutOwnership(QLayout *layout, QWidget *widget)
{
    if (layout == nullptr || widget == nullptr) {
        PyErr_SetString(PyExc_RuntimeError, msgInvalidParameterAdd);
        return;
    }

    //transfer ownership to parent widget
    QWidget *lw = layout->parentWidget();
    QWidget *pw = widget->parentWidget();

   Shiboken::AutoDecRef pyChild(Shiboken::Conversions::pointerToPython(Shiboken::Module::get(SbkPySide6_QtWidgetsTypeStructs[SBK_QWidget_IDX]), widget));

    //Transfer parent to layout widget
    if (pw && lw && pw != lw)
        Shiboken::Object::setParent(nullptr, pyChild);

    if (!lw && !pw) {
        //keep the reference while the layout is orphan
        Shiboken::AutoDecRef pyParent(Shiboken::Conversions::pointerToPython(Shiboken::Module::get(SbkPySide6_QtWidgetsTypeStructs[SBK_QWidget_IDX]), layout));
        Shiboken::Object::keepReference(reinterpret_cast<SbkObject *>(pyParent.object()),
                                        retrieveObjectName(pyParent).constData(),
                                        pyChild, true);
    } else {
        if (!lw)
            lw = pw;
        Shiboken::AutoDecRef pyParent(Shiboken::Conversions::pointerToPython(Shiboken::Module::get(SbkPySide6_QtWidgetsTypeStructs[SBK_QWidget_IDX]), lw));
        Shiboken::Object::setParent(pyParent, pyChild);
    }
}

inline void addLayoutOwnership(QLayout *layout, QLayoutItem *item)
{

    if (layout == nullptr || item == nullptr) {
        PyErr_SetString(PyExc_RuntimeError, msgInvalidParameterAdd);
        return;
    }

    if (QWidget *w = item->widget()) {
        addLayoutOwnership(layout, w);
    } else {
        if (QLayout *l = item->layout())
            addLayoutOwnership(layout, l);
    }

    Shiboken::AutoDecRef pyParent(Shiboken::Conversions::pointerToPython(Shiboken::Module::get(SbkPySide6_QtWidgetsTypeStructs[SBK_QLayout_IDX]), layout));
    Shiboken::AutoDecRef pyChild(Shiboken::Conversions::pointerToPython(Shiboken::Module::get(SbkPySide6_QtWidgetsTypeStructs[SBK_QLayoutItem_IDX]), item));
    Shiboken::Object::setParent(pyParent, pyChild);
}